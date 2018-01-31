# Python version 2 and version 3 compatibility
from __future__ import (absolute_import, division, print_function, unicode_literals)

import os
import sys
import web
import mysql.connector

from lang import Answers, Commands, LangError
from sql import Database
from helper import Params, Zomato
from ciscosparkapi import CiscoSparkAPI, Webhook, SparkApiError
from googletrans import Translator

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
            os.environ[var]
    except KeyError as err:
        system_error(err, "Please set the environment variable " + var + ".")


def init_spark():
    api = object()
    try:
        api = CiscoSparkAPI()
    except SparkApiError as err:
        system_error(err, "Unable to initialize Cisco Spark API.")
    return api


def check_webhooks():
    # Creating webhooks if not existing
    print("INFO: Checking lunch menu webhooks with Spark.")
    required_webhooks = [
        "messages created",
        "messages deleted",
        "memberships created",
        "memberships deleted"
    ]
    try:
        webhooks = p.spark.webhooks.list()
        existing_webhooks = list()
        for hook in webhooks:
            existing_webhooks.append(hook.resource + " " + hook.event)

        # Finding missing webhooks by intersecting two sets
        missing_webhooks = list(set(required_webhooks) - set(existing_webhooks))

        # Creating missing webhooks
        for hook in missing_webhooks:
            p.spark.webhooks.create(
                name=hook,
                targetUrl=os.environ['LUNCHMENU_URL'],
                resource=hook.split()[0],
                event=hook.split()[1]
            )
            print("INFO: Webhook '" + hook + "' successfully created.")
    except SparkApiError as err:
        system_error(err, "Cannot verify lunch menu webhooks with Spark.")


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


def init_params():
    # Getting information about me
    p.me = p.spark.people.me()

    # Inserting or updating bot user
    data = (p.me.id, os.environ['ADMIN_ROOM'], p.me.displayName, p.me.emails[0], os.environ['ADMIN_ROOM'])
    p.db.insert_user(data)

    # Initiating Zomato API
    p.zomato = Zomato(os.environ['ZOMATO_KEY'])

    # Initiating Google Translate API
    p.google = Translator()


def insert_room(data):
    try:
        room = p.spark.rooms.get(data.roomId)
        print("INFO: New membership created, updating database information.")
    except SparkApiError as err:
        print("ERROR: Cannot retrieve room '{0}' detailed information from Spark.".format(data.roomId))
        print(err)
        return

    # Inserting new or updating user
    insert_user(data, room)

    # Inserting new room in the database
    room_data = (room.id, data.id, room.title, room.type)
    p.db.insert_room(room_data)

    # Sending welcome message in English
    ans = Answers('en')
    cmd = Commands('en')
    if room.type == "direct":
        send_message(data.roomId, ans.welcome_direct.format(data.personEmail, cmd.help))
    else:
        send_message(data.roomId, ans.welcome_group.format(p.me.emails[0], cmd.help))


def update_room(data):
    print("INFO: Membership deleted, updating room database.")
    room_data = (0, data.roomId)
    p.db.update_room(room_data)


def insert_user(data, room):
    # Group conversations is not bind to a specific user, but the bot itself
    if room.type == "group":
        return

    try:
        person = p.spark.people.get(data.personId)
    except SparkApiError as err:
        print("ERROR: Cannot retrieve person '{0}' detailed information from Spark.".format(data.personId))
        print(err)
        return

    print("INFO: Inserting or updating user database.")
    user_data = (person.id, room.id, person.displayName, person.emails[0], room.id)
    p.db.insert_user(user_data)


def process_message(data):
    message = p.spark.messages.get(data.id)

    # Loop prevention mechanism, do not respond to my own messages
    if message.personId == p.me.id:
        return
    else:
        print("INFO: New message from <{0}>: '{1}'.".format(message.personEmail, message.text))
        # Get basic information about the user from the database
        r = p.db.select_room([data.roomId])
        if not r:
            print("ERROR: Cannot get the room data.")
            return
        try:
            ans = Answers(r.room_lang)
            cmd = Commands(r.room_lang)
        except LangError as err:
            print("ERROR: Cannot determine language for the given user.")
            print(err)
            return

        text = message.text
        # Trimming the mention tag
        if data.roomType == "group":
            text = str(" ").join(text.split()[1:])

        # Parsing the message received from the user
        msg = parse_message(text)

        # Add restaurant command to the list
        if msg['cmd'] == cmd.add:
            if not add_rest(r, msg['text']):
                send_message(r.room_id, ans.bad_search.format(cmd.search, cmd.add))
            else:
                send_message(r.room_id, ans.add_success.format(cmd.list))

        # Delete restaurant command from the list
        elif msg['cmd'] == cmd.delete:
            if not delete_rest(r, msg['text']):
                send_message(r.room_id, ans.bad_param)
            else:
                send_message(r.room_id, ans.del_success)

        # Sends help message
        elif msg['cmd'] == cmd.help:
            help = ans.help.format(
                data.personEmail,
                cmd.add,
                cmd.delete,
                cmd.help,
                cmd.lang,
                cmd.list,
                cmd.menu,
                cmd.search,
                cmd.all
            )
            send_message(data.roomId, help)

        # Set lunch menu bot language
        elif msg['cmd'] == cmd.lang:
            if not ans.check_lang(msg['text'][0]):
                send_message(r.room_id, ans.lang_unsupported.format(cmd.help))
            else:
                set_lang(r, msg['text'][0])

        # List your favourite restaurants
        elif msg['cmd'] == cmd.list:
            if not list_rest(r):
                send_message(r.room_id, ans.list_empty)

        # Get the menu from the restaurant
        elif msg['cmd'] == cmd.menu:
            if msg['text'][0] == cmd.all:
                if not get_menus(r, ans.no_menu):
                    send_message(r.room_id, ans.bad_param)
            else:
                rest_id = get_restaurant(r, msg['text'][0])
                if rest_id == 0:
                    send_message(r.room_id, ans.bad_param)
                else:
                    menu = get_menu(r, rest_id, ans.no_menu)
                    send_message(r.room_id, menu)

        # Search for a restaurant
        elif msg['cmd'] == cmd.search:
            if not search_rest(r, msg['text']):
                send_message(r.room_id, ans.not_found)
        else:
            print("WARNING: Unknown command received, sending the bot capabilities.")
            send_message(r.room_id, ans.unknown.format(cmd.help))


def message_deleted(data):
    try:
        person = p.spark.people.get(data.personId)
        print("INFO: User " + person.displayName + " has deleted its own message.")
    except SparkApiError as err:
        print("ERROR: Cannot retrieve person '{0}' detailed information from Spark.".format(data.personId))
        print(err)


def parse_message(text):
    tmp = text.split()
    if len(tmp) == 0:
        msg = {'cmd': "Unknown"}
        return msg
    elif len(tmp) == 1:
        msg = {'cmd': tmp[0]}
        return msg
    else:
        msg = {'cmd': tmp[0], 'text': tmp[1:]}

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


def get_menu(r, rest_id, empty):
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
            translation = p.google.translate(dish['dish']['name'], dest=r.room_lang)
            msg += "- **{0}** - {1}\n".format(translation.text, dish['dish']['price'])
        return msg


def get_menus(r, empty):
    # Get the list of all favourite restaurants based on the given room
    restaurants = p.db.select_restaurant([r.room_id])

    if not restaurants:
        return False

    # Due to error with language encoding, the line has to be decoded first
    empty = "- **" + empty.decode('utf-8') + "**"
    menus = str()
    for rest in restaurants:
        menus += "## {0}\n\n".format(rest[1])
        menus += get_menu(r, rest[0], empty)
        menus += "\n\n"

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
    res = p.zomato.search(val)
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


def set_lang(r, lang):
    # Updating language in the database
    data = (lang, r.room_id)
    p.db.update_lang(data)

    # Sending message in the newly set language
    ans = Answers(lang)
    cmd = Commands(lang)
    send_message(r.room_id, ans.lang_set.format(cmd.help))


def send_message(room, msg):
    try:
        p.spark.messages.create(roomId=room, markdown=msg)
    except SparkApiError as err:
        print("WARNING: Cannot send message to the Spark user.")
        print(err)


class Lunchmenu(object):
    def POST(self):
        print("INFO: New HTTP POST request received.")

        # Creating webhook object
        try:
            webhook = Webhook(web.data())
        except SparkApiError as err:
            print("WARNING: Invalid server request, not a JSON format.")
            print(err)
            return

        # Loop prevention, do not react to events triggered by myself
        if webhook.data.personId == p.me.id:
            return

        print("INFO: Spark webhook received - {} {}.".format(webhook.resource, webhook.event))

        # Memberships event
        if webhook.resource == "memberships":
            if webhook.event == "created":
                insert_room(webhook.data)
            elif webhook.event == "deleted":
                update_room(webhook.data)
            else:
                print("WARNING: Unknown memberships webhook event, discarding request.")

        # Messages event
        elif webhook.resource == "messages":
            if webhook.event == "created":
                process_message(webhook.data)
            elif webhook.event == "deleted":
                message_deleted(webhook.data)
            else:
                print("WARNING: Unknown memberships webhook event, discarding request.")

        # Unknown event
        else:
            print("WARNING: Unknown webhook event, discarding event.")


# Main function starting the web.py web server
if __name__ == '__main__':
    check_environment()
    p.spark = CiscoSparkAPI()
    check_webhooks()
    p.db = init_database()
    init_params()

    urls = ('/api/lunchmenu', 'Lunchmenu')
    app = web.application(urls, globals())
    app.run()
