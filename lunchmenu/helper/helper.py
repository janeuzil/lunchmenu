import json
import requests


class Params(object):
    def __init__(self):
        self.spark = object()
        self.zomato = object()
        self.google = object()
        self.db = object()
        self.me = object()
        self.var = [
            "LUNCHMENU_URL",
            "SPARK_ACCESS_TOKEN",
            "ADMIN_ROOM",
            "ZOMATO_KEY",
            "DB_HOST",
            "DB_NAME",
            "DB_USER",
            "DB_PASSWD"
        ]


class Zomato(object):
    def __init__(self, key):
        self.key = key
        self.url_search = "https://developers.zomato.com/api/v2.1/search"
        self.url_rest = "https://developers.zomato.com/api/v2.1/restaurant"
        self.url_menu = "https://developers.zomato.com/api/v2.1/dailymenu"

    def search(self, rest):
        headers = {'Accept': 'application/json', 'user-key': self.key}
        params = {'q': rest, 'entity_id': 84, 'entity_type': 'city', 'count': 5}
        data = json.loads(requests.get(self.url_search, params=params, headers=headers).text)
        return data

    def restaurant(self, rest_id):
        headers = {'Accept': 'application/json', 'user-key': self.key}
        params = {'res_id': rest_id}
        data = json.loads(requests.get(self.url_rest, params=params, headers=headers).text)
        return data

    def menu(self, rest_id):
        headers = {'Accept': 'application/json', 'user-key': self.key}
        params = {'res_id': rest_id}
        data = json.loads(requests.get(self.url_menu, params=params, headers=headers).text)
        return data
