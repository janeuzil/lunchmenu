# Python version 2 and version 3 compatibility
from __future__ import (absolute_import, division, print_function, unicode_literals)

import os
import sys
import re
import web
import signal
import mysql.connector


from datetime import datetime, timedelta
from time import sleep
from threading import Thread, Event
from lang import Answers, Commands, LangError
from sql import Database
from helper import Params, Zomato, Websites
from ciscosparkapi import CiscoSparkAPI, Webhook, SparkApiError
from google.cloud import translate

__author__ = "Jan Neuzil"
__author_email__ = "janeuzil@cisco.com"
__contributors__ = [
    "Daniel Brlekovic <dbrlekov@cisco.com>",
    "Milan Raso <miraso@cisco.com>",
    "Osama Hantool <ohantool@cisco.com>"
]
__copyright__ = "Copyright (c) 2018 Cisco and/or its affiliates."
__license__ = "MIT"

# Global parameters variable
p = Params()


def system_error(err, msg):
    print("ERROR: " + msg)
    print(err)
    sys.exit(1)


def check_environment():
    print("INFO: Checking lunch menu environment variables.")
    var = str()
    try:
        for var in p.var:
            if var in os.environ:
                pass
    except KeyError as err:
        system_error(err, "Please set the environment variable " + var + ".")


def init_spark():
    api = object()
    try:
        api = CiscoSparkAPI()
    except SparkApiError as err:
        system_error(err, "Unable to initialize Cisco Webex Teams API.")
    return api


def check_webhooks():
    # Creating webhooks if not existing
    print("INFO: Checking lunch menu webhooks with Webex Teams.")
    required_webhooks = [
        "messages created",
        "messages deleted",
        "memberships created",
        "memberships deleted"
    ]
    try:
        webhooks = p.webex.webhooks.list()
        existing_webhooks = list()
        for hook in webhooks:
            existing_webhooks.append(hook.resource + " " + hook.event)

        # Finding missing webhooks by intersecting two sets
        missing_webhooks = list(set(required_webhooks) - set(existing_webhooks))

        # Creating missing webhooks
        for hook in missing_webhooks:
            p.webex.webhooks.create(
                name=hook,
                targetUrl=os.environ['LUNCHMENU_URL'],
                resource=hook.split()[0],
                event=hook.split()[1]
            )
            print("INFO: Webhook '" + hook + "' successfully created.")
    except SparkApiError as err:
        system_error(err, "Cannot verify lunch menu webhooks with Webex Teams.")


def init_database():
    print("INFO: Connecting to the internal database.")
    # Connecting to the database and creating tables if they do not exist
    db = object()
    try:
        db = Database(
            os.environ['DB_HOST'],
            os.environ['DB_USER'],
            os.environ['DB_PASSWD'],
            os.environ['DB_NAME']
        )
        db.create_tables()
    except mysql.connector.Error as err:
        system_error(err, "Cannot initialize the database.")

    return db


def check_database():
    print("INFO: Checking if all the rooms are in the database.")

    try:
        # Getting all rooms from Webex Teams
        rooms_wt = p.webex.rooms.list(max=1000)

    except SparkApiError as err:
        system_error(err, "Cannot retrieve list of rooms from the Webex Teams.")

    try:
        # Selecting all rooms from the database
        rooms_db = p.db.select_rooms()

    except mysql.connector.Error as err:
        system_error(err, "Cannot get data from the database.")

    # Get only the list of room ID from the database
    rooms_id = [r[0] for r in rooms_db]

    for room in rooms_wt:
        if room.id not in rooms_id:
            print("WARNING: Correcting missing database entry for the room id {0}".format(room.id))
            if room.type == "direct":
                person = room.creatorId
            else:
                person = p.me.id

            # Get memberships details
            try:
                membership = p.webex.memberships.list(roomId=room.id, personId=person)
                for data in membership:
                    insert_room(data)
            except SparkApiError as err:
                system_error(err, "Cannot retrieve list of rooms from the Webex Teams.")


def init_params():
    # Getting information about me
    p.me = p.webex.people.me()

    # Get the admin room ID
    p.admin = os.environ['ADMIN_ROOM']

    # Inserting or updating bot user
    data = (p.me.id, p.admin, p.me.displayName, p.me.emails[0], p.admin)
    p.db.insert_user(data)

    # Initiating Zomato API
    p.zomato = Zomato(os.environ['ZOMATO_KEY'])

    # Initiating extra websites not updated on Zomato
    p.websites = Websites()

    # Initiating Google Translate API
    p.google = translate.Client()

    p.tz = int(os.environ['TIME_ZONE'])

    # Setting the default value at start
    p.lunch = check_time()


def insert_room(data):
    try:
        room = p.webex.rooms.get(data.roomId)
        print("INFO: New membership created, updating database information.")
    except SparkApiError as err:
        msg = "ERROR: Cannot retrieve room '{0}' detailed information from Webex Teams.\n".format(data.roomId) + str(err)
        print(msg)
        send_message(p.admin, msg)
        return

    # Inserting new or updating user
    user_name = insert_user(data, room)

    # Inserting new room in the database
    room_data = (room.id, data.id, room.title, room.type)
    p.db.insert_room(room_data)

    # Sending welcome message in English
    ans = Answers('en')
    cmd = Commands('en')
    if room.type == "direct":
        msg = ans.welcome_direct.format(user_name, cmd.search, cmd.add, cmd.list, cmd.menu, cmd.vote, cmd.help)
        send_message(data.roomId, msg)
    else:
        msg = ans.welcome_group.format(p.me.emails[0], cmd.search, cmd.add, cmd.list, cmd.menu, cmd.vote, cmd.help)
        send_message(data.roomId, msg)


def update_room(r):
    print("INFO: Membership deleted in direct room, updating room database.")
    room_data = (0, r.room_id)
    p.db.update_room(room_data)


def delete_room(r):
    print("INFO: Membership deleted in group room, deleting from room database.")
    p.db.delete_room([r.room_id])


def get_user(user_id):
    try:
        person = p.webex.people.get(user_id)
        return person
    except SparkApiError as err:
        msg = "ERROR: Cannot retrieve person '{0}' detailed information from Webex Teams.\n".format(user_id) + str(err)
        print(msg)
        send_message(p.admin, msg)
        return None


def insert_user(data, room):
    # Group conversations is not bind to a specific user, but the bot itself
    if room.type == "group":
        return str()

    person = get_user(data.personId)
    if person:
        print("INFO: Inserting or updating user database.")
        user_data = (person.id, room.id, person.displayName, person.emails[0], room.id)
        p.db.insert_user(user_data)
        return person.displayName
    else:
        return str()


def process_message(data):
    message = p.webex.messages.get(data.id)

    # Loop prevention mechanism, do not respond to my own messages
    if message.personId == p.me.id:
        return
    else:
        # Get basic information about the room from the database
        r = p.db.select_room([data.roomId])

        if not r:
            msg = "ERROR: Cannot get the room data - '{0}'.".format(data.roomId)
            print(msg)
            send_message(p.admin, msg)
            return
        print("INFO: New message in the room '{0}' by '<{1}>': '{2}'.".format(
            r.room_name, message.personEmail, message.text)
        )
        try:
            ans = Answers(r.room_lang)
            cmd = Commands(r.room_lang)
        except LangError as err:
            msg = "ERROR: Cannot determine language for the given user.\n" + str(err)
            print(msg)
            send_message(p.admin, msg)
            return

        text = message.text
        # Trimming the mention tag
        if data.roomType == "group":
            text = str(" ").join(text.split()[1:])

        # Parsing the message received from the user
        msg = parse_message(text)

        # Add restaurant command to the list
        if msg['cmd'] == cmd.add:
            if not msg['text'] or not add_rest(r, msg['text']):
                send_message(r.room_id, ans.bad_search.format(cmd.search, cmd.add))
            else:
                send_message(r.room_id, ans.add_success.format(cmd.list))

        # Delete restaurant command from the list
        elif msg['cmd'] == cmd.delete:
            if not msg['text'] or not delete_rest(r, msg['text']):
                send_message(r.room_id, ans.bad_param)
            else:
                send_message(r.room_id, ans.del_success)

        # Sends help message
        elif msg['cmd'] == cmd.help:
            u = get_user(message.personId)
            if not u:
                name = str()
            else:
                name = u.displayName
            help = ans.help.format(
                name,
                cmd.add,
                cmd.delete,
                cmd.help,
                cmd.city,
                cmd.lang,
                cmd.list,
                cmd.menu,
                cmd.recur,
                cmd.search,
                cmd.vote
            )
            send_message(data.roomId, help)

        # Set the city for searching
        elif msg['cmd'] == cmd.city:
            if not msg['text'] or not set_city(r, msg['text']):
                send_message(r.room_id, ans.city_unknown)

        # Set lunch menu bot language
        elif msg['cmd'] == cmd.lang:
            if not msg['text'] or not ans.check_lang(msg['text'][0]):
                send_message(r.room_id, ans.lang_unsupported.format(cmd.help))
            else:
                set_lang(r, msg['text'][0])

        # List your favourite restaurants
        elif msg['cmd'] == cmd.list:
            if not list_rest(r):
                send_message(r.room_id, ans.list_empty)

        # Get the menu from the restaurant
        elif msg['cmd'] == cmd.menu:
            # Empty parameter, fetch all menus
            if not msg['text']:
                if not get_menus(r, ans.no_menu):
                    send_message(r.room_id, ans.bad_param)
            else:
                rest_id = get_restaurant(r, msg['text'][0])
                if rest_id == 0:
                    send_message(r.room_id, ans.bad_param)
                else:
                    menu = get_menu(r, rest_id, ans.no_menu)
                    send_message(r.room_id, menu)

        # Set or unset automatic sending of daily menus at given time every day
        elif msg['cmd'] == cmd.recur:
            set_recurrence(r, msg['text'])

        # Search for a restaurant
        elif msg['cmd'] == cmd.search:
            if not search_rest(r, msg['text']):
                send_message(r.room_id, ans.not_found)

        # Vote for a restaurant
        elif msg['cmd'] == cmd.vote:
            if not msg['text'] or get_restaurant(r, msg['text'][0]) == 0:
                send_message(r.room_id, ans.bad_param)
            else:
                # Time is after lunch hours
                if not check_time():
                    send_message(r.room_id, ans.vote_late)
                # Time is before lunch hours
                else:
                    # Optional time is provided
                    if len(msg['text']) > 1:
                        date = get_time(msg['text'][1], True)
                        if not date:
                            date = set_time(12, 0)
                            send_message(r.room_id, ans.no_time)
                    # Setting default time
                    else:
                        date = set_time(12, 0)
                        send_message(r.room_id, ans.no_time)

                    # Voting for the restaurant
                    if not set_vote(r, msg['text'][0], date):
                        send_message(r.room_id, ans.bad_param)
                    else:
                        send_message(r.room_id, ans.vote_success)

        else:
            print("WARNING: Unknown command received, sending the bot capabilities.")
            send_message(r.room_id, ans.unknown.format(cmd.help))


def message_deleted(data):
    try:
        person = p.webex.people.get(data.personId)
        print("INFO: User " + person.displayName + " has deleted its own message.")
    except SparkApiError as err:
        msg = "ERROR: Cannot retrieve person '{0}' detailed information from Webex Teams.\n".format(data.personId) + str(err)
        print(msg)
        send_message(p.admin, msg)


def parse_message(text):
    tmp = text.split()
    if len(tmp) == 0:
        msg = {'cmd': "Unknown"}
        return msg
    elif len(tmp) == 1:
        msg = {'cmd': tmp[0].lower(), 'text': None}
        return msg
    else:
        msg = {'cmd': tmp[0].lower(), 'text': tmp[1:]}

    return msg


def add_rest(r, val):
    # Finding restaurant ID from the previous search
    data = (r.room_id, val[0])
    rest_id = p.db.select_search(data)
    if not rest_id:
        return False

    # Getting detailed information about the restaurant
    res = p.zomato.restaurant(rest_id)

    # Inserting restaurant details in the database of restaurants
    data = (res['id'], res['name'], res['location']['address'], res['id'])
    p.db.insert_restaurant(data)

    # Inserting restaurant into the room favourites database
    data = (r.room_id, res['id'], r.room_id)
    p.db.insert_favourite(data)
    return True


def delete_rest(r, val):
    rest_id = get_restaurant(r, val[0])
    if rest_id == 0:
        return False

    # Deleting favourite restaurant based on the restaurant ID
    data = (r.room_id, rest_id)
    p.db.delete_favourite(data)
    return True


def get_restaurant(r, val):
    # Get the list of favourite restaurants based on the given room
    restaurants = p.db.select_restaurant([r.room_id])

    # No restaurants found
    if not restaurants:
        return 0

    # Checking the provided value
    try:
        i = int(val)
    except ValueError:
        return 0

    # Checking if provided value does not exceeds number of restaurants
    if i < 0 or i > len(restaurants):
        return 0

    return restaurants[i-1][0]


def format_menu(dish):
    if dish['price']:
        return "- **{0}** - {1}\n".format(dish['name'].strip(" *").rstrip('\r\n'), dish['price'])
    else:
        return "- **{0}**\n".format(dish['name'].strip(" *").rstrip('\r\n'))


def get_menu(r, rest_id, empty):
    # Check if the daily menu for the given language is already in the cache
    menu = p.db.select_menu([rest_id, r.room_lang])
    if menu:
        return menu[0][0]

    # Check if the restaurant is in the exception list
    if rest_id in p.websites.restaurants:
        day = datetime.today().weekday()
        # Some websites might change their HTML code, it can generate error
        try:
            dishes = p.websites.get_menu(rest_id, day)
            msg = str()
            for dish in dishes:
                # Translating dish into desired language using autodetect of Google Translate API
                translation = p.google.translate(dish['name'], target_language=r.room_lang)
                dish['name'] = translation['translatedText']
                msg += format_menu(dish)

                # Store the menu in the cache using database
                data = (rest_id, r.room_lang, msg, msg)
                p.db.insert_menu(data)
            return msg

        except Exception as err:
            print("ERROR: Cannot get the menu from the restaurant - {0}".format(rest_id))
            print(err)
            return empty

    # Get the menus from the Zomato
    menu = p.zomato.menu(rest_id)

    # Some restaurant do not provide daily menus, this option is available only in Czech Republic
    if not menu['status'] == "success":
        return empty

    if not menu['daily_menus']:
        return empty
    else:
        msg = str()
        for dish in menu['daily_menus'][0]['daily_menu']['dishes']:
            # Translating dish into desired language using autodetect of Google Translate API
            translation = p.google.translate(dish['dish']['name'], target_language=r.room_lang)
            dish['dish']['name'] = translation['translatedText']
            msg += format_menu(dish['dish'])

        # Store the menu in the cache using database
        data = (rest_id, r.room_lang, msg, msg)
        p.db.insert_menu(data)
        return msg


def get_menus(r, empty):
    # Get the list of all favourite restaurants based on the given room
    restaurants = p.db.select_restaurant([r.room_id])

    if not restaurants:
        return False

    empty = "- **" + empty + "**"
    menus = str()
    for rest in restaurants:
        menus += "## {0}\n\n".format(rest[1])
        menus += get_menu(r, rest[0], empty)
        menus += "\n\n"

        # Webex Teams does not support messages longer than 10000 characters with encryption
        if len(menus) > 5000:
            send_message(r.room_id, menus)
            menus = str()

    send_message(r.room_id, menus)
    return True


def list_rest(r):
    # Get the list of favourite restaurants based on the given room
    restaurants = p.db.select_restaurant([r.room_id])

    # No restaurants found
    if not restaurants:
        return False

    i = 1
    msg = str()
    for rest in restaurants:
        msg += "{0}. **{1}** - {2}\n".format(i, rest[1], rest[2])
        i += 1
    send_message(r.room_id, msg)
    return True


def search_rest(r, val):
    # Delete previous search result of given user
    p.db.delete_search([r.room_id])

    # Search for restaurant by given name
    res = p.zomato.search(val, r.room_city)

    # Unknown error occurred during the Zomato API call
    if not res:
        return False

    i = 1
    msg = str()
    for rest in res['restaurants']:
        data = (r.room_id, rest['restaurant']['id'], i)
        p.db.insert_search(data)
        msg += "{0}. **{1}** - {2}\n".format(i, rest['restaurant']['name'], rest['restaurant']['location']['address'])
        i += 1

    if res['results_found'] > 0:
        send_message(r.room_id, msg)
        return True
    else:
        return False


def set_city(r, val):
    res = p.zomato.cities(val)

    # City not found
    if not res or not res['location_suggestions']:
        return False

    # Update city with the first result found
    city = res['location_suggestions'][0]
    data = (city['id'], r.room_id)
    p.db.update_city(data)

    ans = Answers(r.room_lang)
    send_message(r.room_id, ans.city_set.format("{0} ({1})".format(city['name'], city['country_name'])))
    return True


def set_lang(r, lang):
    # Czech language exception, Google translate uses 'cs' instead of 'cz'
    if lang == "cz":
        lang = "cs"

    # Updating language in the database
    data = (lang, r.room_id)
    p.db.update_lang(data)

    # Sending message in the newly set language
    ans = Answers(lang)
    cmd = Commands(lang)
    send_message(r.room_id, ans.lang_set.format(cmd.help))


def set_recurrence(r, recurrence_time):
    ans = Answers(r.room_lang)
    flag = False
    default = datetime.now().replace(hour=11, minute=0, second=0, microsecond=0) - timedelta(hours=p.tz)

    # Set or unset this capability
    if not recurrence_time:
        recurrence = p.db.select_recurrence([r.room_id])
        # Setting automating sending of menus for the given room
        if not recurrence:
            data = (r.room_id, default, 0, default)
            p.db.insert_recurrence(data)
        # Disabling automatic sending of menus for the given room
        else:
            p.db.delete_recurrence([r.room_id])

    # Set or update time of this capability
    else:
        date = get_time(recurrence_time[0], False)
        if not date:
            flag = True
            date = default
        data = (r.room_id, date, 0, date)
        p.db.insert_recurrence(data)

    if not flag:
        send_message(r.room_id, ans.recurrence_set)
    else:
        send_message(r.room_id, ans.recurrence_bad)


def check_time():
    # Lunch menus are not available during weekends
    day = datetime.today().weekday()
    if day > 4:
        return False

    # Check if it is not too late for the lunch menu
    now = datetime.now()
    end = now.replace(hour=15, minute=0, second=0) - timedelta(hours=p.tz)
    return end > now


def flush_cache():
    # Check if it is not too late for the lunch menu
    now = datetime.now() + timedelta(hours=p.tz)
    time = (now - now.replace(hour=0, minute=0, second=0, microsecond=0)).total_seconds()

    # Flushing the cache of daily menus and refreshing the database for new automatic menu sending
    if 0 <= time <= 60:
        print("INFO: It is the new day, deleting stored daily menu dishes from cache memory.")
        p.db.delete_menu()
        p.db.update_recurrences()


def get_time(val, past_time):
    now = datetime.now()
    # Regular expression pattern to match hours and minutes during lunch time
    pattern = "(1[0-4])[ .:-]?([0-5][0-9])?"
    time = re.match(pattern, val.strip())

    if not time:
        return None
    else:
        hour = int(time.group(1))
        minute = 0
        if time.group(2):
            minute = int(time.group(2))
        # Creating the date based on the provided time
        date = now.replace(hour=hour, minute=minute, second=0, microsecond=0) - timedelta(hours=p.tz)

        if not past_time:
            return date

        else:
            # Checking the time frame of provided hour
            if date < now:
                return None
            return date


def set_time(hours, minutes):
    now = datetime.now()
    noon = now.replace(hour=hours, minute=minutes, second=0) - timedelta(hours=p.tz)
    # Set the hour to the next hour if it is after
    if now > noon:
        return now.replace(minute=0, second=0) + timedelta(hours=1)
    # Set default lunch time at noon
    else:
        return noon


def set_vote(r, val, date):
    rest_id = get_restaurant(r, val[0])

    # Inserting vote into the database
    data = (r.room_id, rest_id, date, 0, date)
    p.db.insert_vote(data)

    return True


def send_message(room, msg):
    if not msg:
        msg = "ERROR: Cannot send empty message to the Webex Teams user."
        print(msg)
        send_message(p.admin, msg)
        return
    try:
        p.webex.messages.create(roomId=room, markdown=msg)
    except SparkApiError as err:
        print("WARNING: Cannot send message to the Webex Teams user.")
        print(err)


def server_shutdown(signum, frame):
    raise ServerExit("INFO: Signal {0} has been caught, shutting down server.".format(signum))


class Worker(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.shutdown_flag = Event()

    def run(self):
        while not self.shutdown_flag.is_set():
            # Sleeping for a minute before next checking
            sleep(60)

            # Performing database health check each hour to test MySQL connection
            u = p.db.select_user([p.admin])
            if not u:
                msg = "ERROR: Database connection is broken, cannot retrieve data."
                print(msg)
                send_message(p.admin, msg)

            # Flush menu cache if it is the new day
            flush_cache()

            # Time is after lunch hours
            if not check_time():
                # Delete obsolete votes and be prepared for the next day
                if p.lunch:
                    p.lunch = False
                    print("INFO: Lunch time is over, deleting all votes for today.")
                    p.db.delete_vote()
                # Return itself for the next cycle
                continue
            else:
                p.lunch = True

            # Getting the 15 minutes time frame
            now = datetime.now()
            end = now + timedelta(minutes=15)

            # Sending the menu automatically only during the weekdays
            if datetime.today().weekday() < 5:

                # Retrieving the whole table of recurrences and sending the menu automatically
                recurrences = p.db.select_recurrences()
                if recurrences:
                    for recurrence in recurrences:
                        # Current time is bigger and the menus have not been sent yet
                        if now.time() > recurrence[1].time() and recurrence[2] == 0:
                            r = p.db.select_room([recurrence[0]])
                            ans = Answers(r.room_lang)
                            if not get_menus(r, ans.no_menu):
                                send_message(r.room_id, ans.bad_param)
                            p.db.update_recurrence([r.room_id])

            # Retrieving the whole table of votes
            data = (now, end)
            votes = p.db.select_votes(data)

            # No votes found
            if not votes:
                continue

            # Finding colleagues with the same intent
            for vote in votes:
                ans = Answers(vote[4])
                msg = "## {0}\n\n".format(vote[5])
                # Get others with the same intention
                data = (vote[0], vote[1], now)
                rooms = p.db.select_vote(data)
                if not rooms:
                    msg += ans.no_votes
                else:
                    for room in rooms:
                        hour = (room[4] + timedelta(hours=p.tz)).hour
                        minute = (room[4] + timedelta(hours=p.tz)).minute
                        if room[2] == "direct":
                            u = p.db.select_user([room[0]])
                            msg += "- **{0}** - {1:d}:{2:02d}\n".format(u.user_name, hour, minute)
                        else:
                            msg += "- **{0}** - {1:d}:{2:02d}\n".format(room[1], hour, minute)
                print("INFO: Sending the notification to room {0} about the restaurant {1}.".format(vote[3], vote[5]))
                send_message(vote[0], msg)
                # Updating database of votes, that the message was sent
                data = (vote[0], vote[1])
                p.db.update_votes(data)


class ServerExit(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return repr(self.msg)


class Lunchmenu(object):

    @staticmethod
    def POST():
        print("INFO: New HTTP POST request received.")

        # Creating webhook object
        try:
            webhook = Webhook(web.data())
        except SparkApiError as err:
            print("WARNING: Invalid server request, not a JSON format.")
            print(err)
            return

        # Loop prevention, do not react to events triggered by myself
        if webhook.actorId == p.me.id:
            return

        print("INFO: Webex Teams webhook received - {0} {1}.".format(webhook.resource, webhook.event))

        # Memberships event
        if webhook.resource == "memberships":
            if webhook.event == "created":
                insert_room(webhook.data)
            elif webhook.event == "deleted":
                r = p.db.select_room([webhook.data.roomId])
                if not r:
                    msg = "ERROR: Cannot get the room data - '{0}'.".format(webhook.data.roomId)
                    print(msg)
                    send_message(p.admin, msg)
                    return
                if r.room_type == "direct":
                    update_room(r)
                elif r.room_type == "group":
                    delete_room(r)
            else:
                print("WARNING: Unknown memberships webhook event, discarding request.")

        # Messages event
        elif webhook.resource == "messages":
            if webhook.event == "created":
                process_message(webhook.data)
            elif webhook.event == "deleted":
                message_deleted(webhook.data)
            else:
                print("WARNING: Unknown messages webhook event, discarding request.")

        # Unknown event
        else:
            print("WARNING: Unknown webhook event, discarding event.")


def main():
    # Performing environment and health checks
    check_environment()
    p.webex = CiscoSparkAPI()
    check_webhooks()
    p.db = init_database()
    try:
        init_params()
    except Exception as e:
        system_error(e, "Cannot initialize default parameters.")
    check_database()

    urls = ("/api/lunchmenu", "Lunchmenu")
    app = object()
    thread = object()

    # Registering the signal handlers
    signal.signal(signal.SIGTERM, server_shutdown)
    signal.signal(signal.SIGINT, server_shutdown)

    try:
        thread = Worker()
        thread.start()
        app = web.application(urls, globals())
        app.run()
    except ServerExit as msg:
        # Waiting for the threads
        print(msg)
        print("INFO: Waiting for the thread to finish within a minute.")
        thread.shutdown_flag.set()
        thread.join()
        app.stop()
        print("INFO: Server has been shut down successfully.")
        sys.exit(0)


# Main function starting the web.py web server
if __name__ == '__main__':
    main()
