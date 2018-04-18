import mysql.connector


class Room(object):
    def __init__(self, room_id, room_membership, room_active, room_name, room_type, room_lang):
        self.room_id = room_id
        self.room_membership = room_membership
        self.room_active = room_active
        self.room_name = room_name
        self.room_type = room_type
        self.room_lang = room_lang


class User(object):
    def __init__(self, user_id, room_id, user_name, user_email):
        self.user_id = user_id
        self.room_id = room_id
        self.user_name = user_name
        self.user_email = user_email


class Restaurant(object):
    def __init__(self, rest_id, rest_name, rest_address):
        self.rest_id = rest_id
        self.rest_name = rest_name
        self.rest_address = rest_address


class Database(object):
    def __init__(self, host, user, password, database):
        try:
            self.__db = mysql.connector.connect(
                user=user,
                password=password,
                host=host,
                database=database
            )
        except mysql.connector.Error as err:
            raise err

        self.__tables = self.Tables()
        self.__insert = self.Insert()
        self.__update = self.Update()
        self.__delete = self.Delete()
        self.__select = self.Select()

    def __del__(self):
        self.__db.close()

    def __commit_sql(self, sql, data):
        try:
            cursor = self.__db.cursor()
            cursor.execute(sql, data)
            self.__db.commit()
            cursor.close()
        except mysql.connector.Error as err:
            print("ERROR: Cannot execute SQL command in the database.")
            print(err)

    def __query_sql(self, sql, data):
        result = list()
        try:
            cursor = self.__db.cursor()
            cursor.execute(sql, data)
            result = cursor.fetchall()
            cursor.close()
        except mysql.connector.Error as err:
            print("ERROR: Cannot query SQL command in the database.")
            print(err)
        return result

    def create_tables(self):
        self.__commit_sql(self.__tables.create_rooms(), None)
        self.__commit_sql(self.__tables.create_users(), None)
        self.__commit_sql(self.__tables.create_restaurants(), None)
        self.__commit_sql(self.__tables.create_favourites(), None)
        self.__commit_sql(self.__tables.create_search(), None)
        self.__commit_sql(self.__tables.create_votes(), None)

    def insert_room(self, data):
        self.__commit_sql(self.__insert.insert_room(), data)

    def insert_user(self, data):
        self.__commit_sql(self.__insert.insert_user(), data)

    def insert_restaurant(self, data):
        self.__commit_sql(self.__insert.insert_restaurant(), data)

    def insert_favourite(self, data):
        self.__commit_sql(self.__insert.insert_favourite(), data)

    def insert_search(self, data):
        self.__commit_sql(self.__insert.insert_search(), data)

    def insert_vote(self, data):
        self.__commit_sql(self.__insert.insert_vote(), data)

    def update_room(self, data):
        self.__commit_sql(self.__update.update_room(), data)

    def update_lang(self, data):
        self.__commit_sql(self.__update.update_lang(), data)

    def update_votes(self, data):
        self.__commit_sql(self.__update.update_vote(), data)

    def select_room(self, data):
        result = self.__query_sql(self.__select.select_room(), data)
        if result:
            return Room(result[0][0], result[0][1], result[0][2], result[0][3], result[0][4], result[0][5])
        else:
            return None

    def select_user(self, data):
        result = self.__query_sql(self.__select.select_user(), data)
        if result:
            return User(result[0][1], result[0][1], result[0][2], result[0][3])
        else:
            return None

    def select_restaurant(self, data):
        result = self.__query_sql(self.__select.select_restaurant(), data)
        if result:
            return result
        else:
            return None

    def select_search(self, data):
        result = self.__query_sql(self.__select.select_search(), data)
        if result:
            return result[0][0]
        else:
            return None

    def select_votes(self, data):
        result = self.__query_sql(self.__select.select_votes(), data)
        if result:
            return result
        else:
            return None

    def select_vote(self, data):
        result = self.__query_sql(self.__select.select_vote(), data)
        if result:
            return result
        else:
            return None

    def delete_room(self, data):
        self.__commit_sql(self.__delete.delete_room(), data)

    def delete_search(self, data):
        self.__commit_sql(self.__delete.delete_search(), data)

    def delete_favourite(self, data):
        self.__commit_sql(self.__delete.delete_favourite(), data)

    def delete_vote(self):
        self.__commit_sql(self.__delete.delete_vote(), None)

    class Tables(object):
        def __init__(self):
            self.__rooms = (
                "CREATE TABLE IF NOT EXISTS rooms("
                "room_id VARCHAR(128) NOT NULL,"
                "room_membership VARCHAR(256) NOT NULL,"
                "room_active TINYINT NOT NULL,"
                "room_name VARCHAR(128) COLLATE utf8_unicode_ci NOT NULL,"
                "room_type VARCHAR(16) NOT NULL,"
                "room_lang VARCHAR(4) DEFAULT 'en' NOT NULL,"
                "PRIMARY KEY(room_id))"
            )
            self.__users = (
                "CREATE TABLE IF NOT EXISTS users("
                "user_id VARCHAR(128) NOT NULL,"
                "room_id VARCHAR(128),"
                "user_name VARCHAR(128) NOT NULL,"
                "user_email VARCHAR(32) NOT NULL,"
                "PRIMARY KEY(user_id))"
            )
            self.__restaurants = (
                "CREATE TABLE IF NOT EXISTS restaurants("
                "rest_id INT NOT NULL,"
                "rest_name VARCHAR(64) COLLATE utf8_unicode_ci NOT NULL,"
                "rest_address VARCHAR(128) COLLATE utf8_unicode_ci NOT NULL,"
                "PRIMARY KEY(rest_id))"
            )
            self.__favourites = (
                "CREATE TABLE IF NOT EXISTS favourites("
                "room_id VARCHAR(128) NOT NULL,"
                "rest_id INT NOT NULL,"
                "PRIMARY KEY(room_id, rest_id),"
                "CONSTRAINT room_f_constr FOREIGN KEY room_f_fk(room_id)"
                "REFERENCES rooms(room_id) ON DELETE CASCADE ON UPDATE CASCADE,"
                "CONSTRAINT rest_f_constr FOREIGN KEY rest_f_fk(rest_id)"
                "REFERENCES restaurants(rest_id) ON DELETE CASCADE ON UPDATE CASCADE)"
            )
            self.__search = (
                "CREATE TABLE IF NOT EXISTS search("
                "room_id VARCHAR(128) NOT NULL,"
                "rest_id INT NOT NULL,"
                "rest_num INT NOT NULL,"
                "PRIMARY KEY(room_id, rest_id),"
                "CONSTRAINT room_s_constr FOREIGN KEY room_s_fk(room_id)"
                "REFERENCES rooms(room_id) ON DELETE CASCADE ON UPDATE CASCADE)"
            )
            self.__votes = (
                "CREATE TABLE IF NOT EXISTS votes("
                "room_id VARCHAR(128) NOT NULL,"
                "rest_id INT NOT NULL,"
                "vote_date DATETIME NOT NULL,"
                "vote_sent TINYINT NOT NULL,"
                "PRIMARY KEY(room_id, rest_id),"
                "CONSTRAINT room_v_constr FOREIGN KEY room_v_fk(room_id)"
                "REFERENCES rooms(room_id) ON DELETE CASCADE ON UPDATE CASCADE,"
                "CONSTRAINT rest_v_constr FOREIGN KEY rest_v_fk(rest_id)"
                "REFERENCES restaurants(rest_id) ON DELETE CASCADE ON UPDATE CASCADE)"
            )

        def create_rooms(self):
            return self.__rooms

        def create_users(self):
            return self.__users

        def create_restaurants(self):
            return self.__restaurants

        def create_favourites(self):
            return self.__favourites

        def create_search(self):
            return self.__search

        def create_votes(self):
            return self.__votes

    class Insert(object):
        def __init__(self):
            self.__room = (
                "INSERT INTO rooms (room_id, room_membership, room_active, room_name, room_type)"
                "VALUES (%s, %s, 1, %s, %s) ON DUPLICATE KEY UPDATE room_active = 1"
            )
            self.__user = (
                "INSERT INTO users (user_id, room_id, user_name, user_email)"
                "VALUES (%s, %s, %s, %s) ON DUPLICATE KEY UPDATE room_id = %s"
            )
            self.__restaurant = (
                "INSERT INTO restaurants (rest_id, rest_name, rest_address) VALUES (%s, %s, %s)"
                "ON DUPLICATE KEY UPDATE rest_id = %s"
            )
            self.__favourite = (
                "INSERT INTO favourites (room_id, rest_id) VALUES (%s, %s)"
                "ON DUPLICATE KEY UPDATE room_id = %s"
            )
            self.__search = "INSERT INTO search (room_id, rest_id, rest_num) VALUES (%s, %s, %s)"
            self.__vote = (
                "INSERT INTO votes (room_id, rest_id, vote_date, vote_sent) VALUE (%s, %s, %s, %s)"
                "ON DUPLICATE KEY UPDATE vote_date = %s"
            )

        def insert_room(self):
            return self.__room

        def insert_user(self):
            return self.__user

        def insert_restaurant(self):
            return self.__restaurant

        def insert_favourite(self):
            return self.__favourite

        def insert_search(self):
            return self.__search

        def insert_vote(self):
            return self.__vote

    class Update(object):
        def __init__(self):
            self.__room = "UPDATE rooms SET room_active = %s WHERE room_id = %s"
            self.__lang = "UPDATE rooms SET room_lang = %s WHERE room_id = %s"
            self.__vote = "UPDATE votes SET vote_sent = 1 WHERE room_id = %s AND rest_id = %s"

        def update_room(self):
            return self.__room

        def update_lang(self):
            return self.__lang

        def update_vote(self):
            return self.__vote

    class Delete(object):
        def __init__(self):
            self.__room = "DELETE FROM rooms WHERE room_id = %s"
            self.__search = "DELETE FROM search WHERE room_id = %s"
            self.__favourite = "DELETE FROM favourites WHERE room_id = %s AND rest_id = %s"
            self.__vote = "DELETE FROM votes"

        def delete_room(self):
            return self.__room

        def delete_search(self):
            return self.__search

        def delete_favourite(self):
            return self.__favourite

        def delete_vote(self):
            return self.__vote

    class Select(object):
        def __init__(self):
            self.__room = "SELECT * FROM rooms WHERE room_id = %s"
            self.__user = "SELECT * FROM users WHERE room_id = %s ORDER BY user_email"
            self.__search = "SELECT rest_id FROM search WHERE room_id = %s AND rest_num = %s"
            self.__restaurant = (
                "SELECT r.* FROM restaurants r INNER JOIN favourites f ON r.rest_id = f.rest_id "
                "WHERE f.room_id = %s ORDER BY r.rest_name"
            )
            self.__votes = (
                "SELECT v.room_id, v.rest_id, v.vote_date, ro.room_name, ro.room_lang, re.rest_name "
                "FROM votes v JOIN rooms ro ON v.room_id = ro.room_id JOIN restaurants re ON v.rest_id = re.rest_id "
                "WHERE v.vote_sent = 0 AND v.vote_date BETWEEN %s AND %s"
            )
            self.__vote = (
                "SELECT r.room_id, r.room_name, r.room_type, r.room_lang, v.vote_date "
                "FROM votes v JOIN rooms r ON v.room_id = r.room_id "
                "WHERE v.room_id != %s AND v.rest_id = %s AND v.vote_date > %s"
            )

        def select_room(self):
            return self.__room

        def select_user(self):
            return self.__user

        def select_restaurant(self):
            return self.__restaurant

        def select_search(self):
            return self.__search

        def select_votes(self):
            return self.__votes

        def select_vote(self):
            return self.__vote
