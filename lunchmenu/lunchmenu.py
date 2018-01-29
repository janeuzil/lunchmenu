# Python version 2 and version 3 compatibility
from __future__ import (absolute_import, division, print_function, unicode_literals)

import os
import sys
import web
import mysql.connector

from lang import Answers, Commands, LangError
from sql import Database, User
from helper import Params
from ciscosparkapi import CiscoSparkAPI, Webhook, SparkApiError

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
    # Getting information about me
    p.me = p.api.people.me()

    # Creating webhooks if not existing
    print("INFO: Checking lunch menu webhooks with Spark.")
    required_webhooks = [
        "messages created",
        "messages deleted",
        "memberships created",
        "memberships deleted"
    ]
    try:
        webhooks = p.api.webhooks.list()
        existing_webhooks = list()
        for hook in webhooks:
            existing_webhooks.append(hook.resource + " " + hook.event)

        # Finding missing webhooks by intersecting two sets
        missing_webhooks = list(set(required_webhooks) - set(existing_webhooks))

        # Creating missing webhooks
        for hook in missing_webhooks:
            p.api.webhooks.create(
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

    # Inserting or updating bot user
    data = (p.me.id, os.environ['ADMIN_ROOM'], p.me.displayName, p.me.emails[0], os.environ['ADMIN_ROOM'])
    db.insert_user(data)
    return db


def insert_room(data):
    try:
        room = p.api.rooms.get(data.roomId)
        print("INFO: New membership created, updating database information.")
    except SparkApiError as err:
        print("ERROR: Cannot retrieve room '{}' detailed information from Spark.".format(data.roomId))
        print(err)
        return

    # Inserting new or updating user
    u = insert_user(data, room)

    # Inserting new room in the database
    room_data = (room.id, data.id, room.title, room.type)
    p.db.insert_room(room_data)

    ans = Answers(u.user_lang)
    cmd = Commands(u.user_lang)
    if room.type == "direct":
        send_message(data.roomId, ans.welcome_direct.format(u.user_email, cmd.help))
    else:
        send_message(data.roomId, ans.welcome_group.format(p.me.emails[0], cmd.help))


def update_room(data):
    print("INFO: Membership deleted, updating room database.")
    room_data = (0, data.roomId)
    p.db.update_room(room_data)


def insert_user(data, room):
    # Group conversations is not bind to a specific user, but the bot itself
    if room.type == "group":
        return User(p.me.id, os.environ['ADMIN_ROOM'], p.me.displayName, p.me.emails[0], "en")

    try:
        person = p.api.people.get(data.personId)
    except SparkApiError as err:
        print("ERROR: Cannot retrieve person '{}' detailed information from Spark.".format(data.personId))
        print(err)
        return

    print("INFO: Inserting or updating user database.")
    user_data = (person.id, room.id, person.displayName, person.emails[0], room.id)
    p.db.insert_user(user_data)
    return User(person.id, room.id, person.displayName, person.emails[0], "en")


def process_message(data):
    message = p.api.messages.get(data.id)

    # Loop prevention mechanism, do not respond to my own messages
    if message.personId == p.me.id:
        return
    else:
        print("INFO: New message: '{}'".format(message.text))
        # Get basic information about the user from the database
        u = p.db.select_user([data.personId])
        if not u:
            print("ERROR: Cannot get the user data.")
            return
        try:
            ans = Answers(u.user_lang)
            cmd = Commands(u.user_lang)
        except LangError as err:
            print("ERROR: Cannot determine language for the given user.")
            print(err)
            return

        text = message.text
        # Trimming the mention tag
        if data.roomType == "group":
            text = str().join(text.split()[1:])

        # Parsing the message received from the user
        msg = parse_message(text)

        # Add restaurant command to the list
        if msg['cmd'] == cmd.add:
            add_rest(u, msg['text'])
        # Delete restaurant command from the list
        elif msg['cmd'] == cmd.delete:
            delete_rest(u, msg['text'])
        # Sends help message
        elif msg['cmd'] == cmd.help:
            help = ans.help.format(
                u.user_email,
                cmd.add,
                cmd.delete,
                cmd.help,
                cmd.lang,
                cmd.list,
                cmd.menu,
                cmd.search
            )
            send_message(data.roomId, help)
        # Set menu language
        elif msg['cmd'] == cmd.lang:
            set_lang(u, msg['text'])
        # List your favourite restaurants
        elif msg['cmd'] == cmd.list:
            list_rest(u)
        # Get the menu from the restaurant
        elif msg['cmd'] == cmd.menu:
            get_menu(u, msg['text'])
        # Search for a restaurant
        elif msg['cmd'] == cmd.search:
            search_rest(u, msg['text'])
        else:
            print("WARNING: Unknown command received, sending the bot capabilities.")
            send_message(data.roomId, ans.unknown)


def message_deleted(data):
    try:
        person = p.api.people.get(data.personId)
        print("INFO: User " + person.displayName + " has deleted its own message.")
    except SparkApiError as err:
        print("ERROR: Cannot retrieve person '{}' detailed information from Spark.".format(data.personId))
        print(err)


def parse_message(text):
    print(text)
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


def add_rest(u, val):
    # TODO will check if the user used the searched before, adds the the restaurant into the list
    pass


def delete_rest(u, val):
    # TODO delete restaurant from the list
    pass


def get_menu(u, val):
    # TODO get the daily menu of the restaurant, call Zomato API and then translate it to required language
    pass


def list_rest(u):
    # TODO Select from favourites tables based on the user and printed it in a nice list
    pass


def search_rest(u, val):
    # TODO Search for restaurant, based on the provided name and adds restaurants in the database
    pass


def set_lang(u, val):
    # TODO Set the user language
    pass


def send_message(room, msg):
    try:
        p.api.messages.create(roomId=room, markdown=msg)
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

        if webhook.data.personId != p.me.id:
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
    p.api = CiscoSparkAPI()
    check_webhooks()
    p.db = init_database()

    urls = ('/api/lunchmenu', 'Lunchmenu')
    app = web.application(urls, globals())
    app.run()
