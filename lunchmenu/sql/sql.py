import mysql.connector


class User(object):
    def __init__(self, user_id, room_id, user_name, user_email, user_lang):
        self.user_id = user_id
        self.room_id = room_id
        self.user_name = user_name
        self.user_email = user_email
        self.user_lang = user_lang


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

    def __execute_sql(self, sql, data):
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
        self.__execute_sql(self.__tables.create_rooms(), None)
        self.__execute_sql(self.__tables.create_users(), None)
        self.__execute_sql(self.__tables.create_restaurants(), None)
        self.__execute_sql(self.__tables.create_favourites(), None)
        self.__execute_sql(self.__tables.create_search(), None)

    def insert_room(self, data):
        self.__execute_sql(self.__insert.insert_room(), data)

    def insert_user(self, data):
        self.__execute_sql(self.__insert.insert_user(), data)

    def update_room(self, data):
        self.__execute_sql(self.__update.update_room(), data)

    def select_user(self, data):
        result = self.__query_sql(self.__select.select_user(), data)
        if result:
            return User(result[0][1], result[0][1], result[0][2], result[0][3], result[0][4])
        else:
            return None

    class Tables(object):
        def __init__(self):
            self.__rooms = (
                "CREATE TABLE IF NOT EXISTS rooms("
                "room_id VARCHAR(128) NOT NULL,"
                "room_membership VARCHAR(256) NOT NULL,"
                "room_active TINYINT NOT NULL,"
                "room_name VARCHAR(128) NOT NULL,"
                "room_type VARCHAR(16) NOT NULL,"
                "PRIMARY KEY(room_id))"
            )
            self.__users = (
                "CREATE TABLE IF NOT EXISTS users("
                "user_id VARCHAR(128) NOT NULL,"
                "room_id VARCHAR(128),"
                "user_name VARCHAR(128) NOT NULL,"
                "user_email VARCHAR(32) NOT NULL,"
                "user_lang VARCHAR(4) NOT NULL,"
                "PRIMARY KEY(user_id))"
            )
            self.__restaurants = (
                "CREATE TABLE IF NOT EXISTS restaurants("
                "rest_id INT NOT NULL,"
                "rest_name VARCHAR(128) NOT NULL,"
                "PRIMARY KEY(rest_id))"
            )
            self.__favourites = (
                "CREATE TABLE IF NOT EXISTS favourites("
                "user_id VARCHAR(128) NOT NULL,"
                "rest_id INT NOT NULL,"
                "PRIMARY KEY(user_id, rest_id),"
                "CONSTRAINT user_constr FOREIGN KEY user_fk(user_id)"
                "REFERENCES users(user_id) ON DELETE CASCADE ON UPDATE CASCADE,"
                "CONSTRAINT rest_constr FOREIGN KEY rest_fk(rest_id)"
                "REFERENCES restaurants(rest_id) ON DELETE CASCADE ON UPDATE CASCADE)"
            )
            self.__search = (
                "CREATE TABLE IF NOT EXISTS search("
                "user_id VARCHAR(128) NOT NULL,"
                "rest_id INT NOT NULL,"
                "PRIMARY KEY(user_id),"
                "FOREIGN KEY (user_id)"
                "REFERENCES users(user_id) ON DELETE CASCADE ON UPDATE CASCADE)"
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

    class Insert(object):
        def __init__(self):
            self.__rooms = (
                "INSERT INTO rooms (room_id, room_membership, room_active, room_name, room_type)"
                "VALUES (%s, %s, 1, %s, %s) ON DUPLICATE KEY UPDATE room_active = 1"
            )
            self.__users = (
                "INSERT INTO users (user_id, room_id, user_name, user_email, user_lang)"
                "VALUES (%s, %s, %s, %s, 'en') ON DUPLICATE KEY UPDATE room_id = %s"
            )

        def insert_room(self):
            return self.__rooms

        def insert_user(self):
            return self.__users

    class Update(object):
        def __init__(self):
            self.__rooms = "UPDATE rooms SET room_active = %s WHERE room_id = %s"

        def update_room(self):
            return self.__rooms

    class Delete(object):
        def __init__(self):
            self.__search = "DELETE FROM search WHERE user_id = %s"

        def delete_search(self):
            return self.__search

    class Select(object):
        def __init__(self):
            self.__user = "SELECT * FROM users WHERE user_id = %s"

        def select_user(self):
            return self.__user
