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
        menu = str()

        # Get menu for Passage restaurant from their the websites
        if rest_id == 16510287:
            url = "https://www.passage.cz"
            r = requests.get(url)
            tree = html.fromstring(r.content)
            tmp = tree.xpath('//p[@style="text-align: center;"]/text()')

            # Price is always behind the actual dish
            pattern = "^[0-9]{2,3}.*"
            dishes = list()
            for i in range(len(tmp)):
                res = re.match(pattern, tmp[i])
                if res:
                    dishes.append(tmp[i-1].strip())
                    dishes.append(tmp[i])

            for i in range(0, len(dishes), 2):
                menu += "- **" + dishes[i] + "** - " + dishes[i + 1] + "\n"
            return menu

        elif rest_id == 16511008:
            url = "http://www.potrefena-husa.eu"
            r = requests.get(url)

            tree = html.fromstring(r.content)

            dishes = tree.xpath('//h4/text()')
            side_dishes = tree.xpath('//p/text()')
            prices = tree.xpath('//span[@class="price"]/text()')

            menu = str()

            for i, j, k in zip(dishes, side_dishes, prices):
                menu += "- **" + i.strip() + " " + j.strip() + "** - " + k.strip() + "\n"
            return menu

        return menu
