import re
import json
import requests
from lxml import html


class Params(object):
    def __init__(self):
        self.spark = object()
        self.zomato = object()
        self.websites = object()
        self.google = object()
        self.db = object()
        self.me = object()
        self.admin = str()
        self.tz = int()
        self.lunch = bool()
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


class Websites(object):
    def __init__(self):
        self.restaurants = (16511008, 16510287)

    def get_menu(self, rest_id):
        dishes = list()

        # Get menu for Passage restaurant from their the websites
        if rest_id == 16510287:
            url = "https://www.passage.cz"
            r = requests.get(url)
            tree = html.fromstring(r.content)
            tmp = tree.xpath('//p[@style="text-align: center;"]/text()')

            # Price is always behind the actual dish
            pattern = "^[0-9]{2,3}.*"
            menu = list()
            for i in range(len(tmp)):
                res = re.match(pattern, tmp[i])
                if res:
                    menu.append(tmp[i-1].strip())
                    menu.append(tmp[i])

            for i in range(0, len(menu), 2):
                dishes.append({'name': menu[i], 'price': menu[i+1]})
            return dishes

        elif rest_id == 16511008:
            url = "http://www.potrefena-husa.eu"
            r = requests.get(url)

            tree = html.fromstring(r.content)

            menu = tree.xpath('//h4/text()')
            sides = tree.xpath('//p/text()')
            prices = tree.xpath('//span[@class="price"]/text()')

            for i, j, k in zip(menu, sides, prices):
                dishes.append({'name': i.strip() + " " + j.strip(), 'price': k.strip()})
            return dishes

        # TODO Add more restaurants

        return dishes
