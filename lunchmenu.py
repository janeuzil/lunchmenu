# Python version 2 and version 3 compatibility
from __future__ import (absolute_import, division, print_function, unicode_literals)

import os
import web
import requests
import mysql.connector

from builtins import *
from ciscosparkapi import CiscoSparkAPI, Webhook, SparkApiError

__author__ = "Jan Neuzil"
__author_email__ = "janeuzil@cisco.com"
__contributors__ = ["Daniel Brlekovic <dbrlekov@cisco.com>", "Milan Raso <miraso@cisco.com>", "Osama Hantool <ohantool@cisco.com>"]
__copyright__ = "Copyright (c) 2018 Cisco and/or its affiliates."
__license__ = "MIT"

# Global variables
db = object()
me = None
variables = ["LUNCHMENU_URL", "SPARK_ACCESS_TOKEN", "DB_HOST", "DB_NAME", "DB_USER", "DB_PASSWD"]
tables = ["CREATE TABLE IF NOT EXISTS rooms("
              " room_id VARCHAR(128) NOT NULL,"
              " room_membership VARCHAR(256) NOT NULL,"
              " room_active TINYINT NOT NULL,"
              " room_name VARCHAR(128) NOT NULL,"
              " room_type VARCHAR(16) NOT NULL,"
              " PRIMARY KEY(room_id))",
          "CREATE TABLE IF NOT EXISTS users("
              " user_id VARCHAR(128) NOT NULL,"
              " room_id VARCHAR(128),"
              " user_name VARCHAR(128) NOT NULL,"
              " user_email VARCHAR(32) NOT NULL,"
              " PRIMARY KEY(user_id))",
          "CREATE TABLE IF NOT EXISTS restaurants("
              " rest_id INT NOT NULL,"
              " rest_name VARCHAR(128) NOT NULL,"
              " PRIMARY KEY(rest_id))",
          "CREATE TABLE IF NOT EXISTS favourites("
              " user VARCHAR(128) NOT NULL,"
              " restaurant INT NOT NULL,"
              " PRIMARY KEY(user, restaurant),"
              " CONSTRAINT user_constr FOREIGN KEY user_fk(user)"
              " REFERENCES users(user_id) ON DELETE CASCADE ON UPDATE CASCADE,"
              " CONSTRAINT rest_constr FOREIGN KEY rest_fk(restaurant)"
              " REFERENCES restaurants(rest_id) ON DELETE CASCADE ON UPDATE CASCADE)"]

def system_error(err, msg):
    print("ERROR: " + msg)
    print(err)
    sys.exit(1)


def check_environment():
    print("INFO: Checking lunchbot environement variables.")
    try:  
        for var in variables:
            os.environ[var]
    except KeyError as err:
        system_error(err, "Please set the environment variable " + var + ".")

def check_webhooks(api):
    global me
    me = api.people.me()

    # Creating webhooks if not existing
    print("INFO: Checking lunchbot webhooks with Spark.")
    required_webhooks = ["messages created", "messages deleted", "memberships created", "memberships deleted"]
    try:
        webhooks = api.webhooks.list()
        existing_webhooks = list()
	for hook in webhooks:
            existing_webhooks.append(hook.resource + " " + hook.event)

        # Finding missing webhooks by intersecting two sets
	missing_webhooks = list(set(required_webhooks) - set(existing_webhooks))

        # Creating missing webhooks
        for hook in missing_webhooks:
            res = api.webhooks.create(name=hook, targetUrl=os.environ["LUNCHMENU_URL"], resource=hook.split()[0], event=hook.split()[1])
            print("INFO: Webhook '" + hook + "' succesfully created.")
    except SparkApiError as err:
        system_error(err, "Cannot verify lunchbot webhooks with Spark.")

def init_database():
    global db
    print("INFO: Connecting to the internal database")
    try:
        db = mysql.connector.connect(user=os.environ["DB_USER"], password=os.environ["DB_PASSWD"], host=os.environ["DB_HOST"], database=os.environ["DB_NAME"])
    except mysql.connector.Error as err:
        system_error(err, "Cannot connect to the database.")

    # Creating tables if they do not exist
    cursor = db.cursor()
    try:
        for sql in tables:
            cursor.execute(sql)
        cursor.close()
    except mysql.connector.Error as err:
        system_error(err, "Cannot create database table.")

def execute_database(sql, sql_data):
    try:
        cursor = db.cursor()
        cursor.execute(sql, sql_data)
        db.commit()
    except mysql.connector.Error as err:
        print("ERROR: Cannot execute SQL command in the database.")
        print(err)

def insert_room(data):
    try:
        room = api.rooms.get(data.roomId)
    except SparkApiError as err:
        print("ERROR: Cannot retrieve room '{}' detailed information from Spark.".format(data.roomId))
        print(err)
        return

    # Inserting new or updating user
    insert_user(data, room)
    sql = "INSERT INTO rooms (room_id, room_membership, room_active, room_name, room_type) " \
          "VALUES (%s, %s, 1, %s, %s) ON DUPLICATE KEY UPDATE room_active = 1"
    sql_data = (room.id, data.id, room.title, room.type);

    execute_database(sql, sql_data)

def update_room(data):
    sql = "UPDATE rooms SET room_active = %d WHERE room_id = %s"
    sql_data = (0, data.roomId)

    execute_database(sql, sql_data)

def insert_user(data, room):
    try:
        person = api.people.get(data.personId)
        print("INFO: User " + person.displayName + " has deleted its own message.")
    except SparkApiError as err:
        print("ERROR: Cannot retrieve person '{}' detailed information from Spark.".format(data.personId))
        return
    if room.type == "direct":
        sql = "INSERT INTO users (user_id, room_id, user_name, user_email) " \
              "VALUES (%s, %s, %s, %s) ON DUPLICATE KEY UPDATE room_id = %s, user_name = %s"
        sql_data = (person.id, room.id, person.displayName, person.emails[0], room.id, person.displayName)
    elif room.type == "group":
        sql = "INSERT INTO users (user_id, user_name, user_email) " \
              "VALUES (%s, %s, %s) ON DUPLICATE KEY UPDATE user_id = %s, user_name = %s"
        sql_data = (person.id, person.displayName, person.emails[0], person.id, person.displayName)
    else:
        print("ERROR: Unknown room type, invalid data received.")
        return

    execute_database(sql, sql_data)

def process_message(data):
    message = api.messages.get(data.id)
    print("INFO: New message: '{}'".format(message.text))

    # Loop prevention mechanism, do not respond to my own messages
    if message.personId == me.id:
        return
    else:
        # TODO Parsing message
        pass

def message_deleted(data):
    try:
        person = api.people.get(data.personId)
        print("INFO: User " + person.displayName + " has deleted its own message.")
    except SparkApiError as err:
        print("ERROR: Cannot retrieve person '{}' detailed information from Spark.".format(data.personId))

class lunchmenu(object):

    def POST(self):
	print("INFO: New HTTP POST request received.")

        # Creating webhook object
        try:
            webhook = Webhook(web.data())
        except SparkApiError as err:
            print("WARNING: Invalid server request, not a JSON format.")
            return

        print("INFO: Spark webhook received - {} {}.".format(webhook.resource, webhook.event))
        # Memberships event
        if webhook.resource == "memberships":
            if webhook.event == "created":
                insert_room(webhook.data)
            elif webhook.event == "deleted":
                update_room(webhook.data)
            else:
                print("WARNING: Unknown memeberships webhook event, discarding request.")

        # Messages event
        elif webhook.resource == "messages":
            if webhook.event == "created":
                process_message(webhook.data)
            elif webhook.event == "deleted":
                message_deleted(webhook.data)
            else:
                print("WARNING: Unknown memeberships webhook event, discarding request.")

        # Unknown event
        else:
            print("WARNING: Unknown webhook event, discarding event.")


# Main function starting the web.py web server
if __name__ == '__main__':
    
    check_environment()
    api = CiscoSparkAPI()
    check_webhooks(api)
    conn = init_database()

    urls = ('/api/lunchmenu', 'lunchmenu')
    app = web.application(urls, globals())
    app.run()
    db.close()
