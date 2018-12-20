import re
import json
import requests
from lxml import html


class Params(object):
    def __init__(self):
        self.webex = object()
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
        self.url_cities = "https://developers.zomato.com/api/v2.1/cities"
        self.url_rest = "https://developers.zomato.com/api/v2.1/restaurant"
        self.url_menu = "https://developers.zomato.com/api/v2.1/dailymenu"

    def search(self, rest, city):
        headers = {'Accept': 'application/json', 'user-key': self.key}
        params = {'q': rest, 'entity_id': city, 'entity_type': 'city', 'count': 5}
        data = json.loads(requests.get(self.url_search, params=params, headers=headers).text)
        return data

    def cities(self, city):
        headers = {'Accept': 'application/json', 'user-key': self.key}
        params = {'q': city}
        data = json.loads(requests.get(self.url_cities, params=params, headers=headers).text)
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
        self.restaurants = (
            16511008,  # Passage
            16510287,  # Potrefena Husa
            18311827,  # Portfolio
            16510105,  # Fiesta
            18291268,  # Rebel Wings
            16506886,  # Hybernia
            18271176,  # Black Dog
            16510118,  # Kolkovna
            16517493,  # Hooters
            16506101,  # La Gare
            16506344,  # Pizza Coloseum
            16506517,  # Na Pekarce
            16506646   # Midtown Grill
        )
        self.week = (
            "monday",
            "tuesday",
            "wednesday",
            "thursday",
            "friday"
        )

    @staticmethod
    def strip_menu(menu):
        menu = map(unicode, menu)
        menu = map(unicode.strip, menu)
        menu = filter(None, menu)
        return menu

    def get_menu(self, rest_id, day):
        # Weekend time
        if day > 4:
            return None

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

        elif rest_id == 18311827:
            url = "http://www.portfolio-restaurant.cz/obedove-menu"
            r = requests.get(url)
            tree = html.fromstring(r.content)

            menu = tree.xpath('//td[@class="btm food-name"]/strong/text()')
            prices = tree.xpath('//td[@class="btm food-price"]/text()')

            for name, price in zip(menu, prices):
                dishes.append({'name': name, 'price': price})
            return dishes

        elif rest_id == 16510105:
            url = "http://www.restaurace-fiesta.cz"
            r = requests.get(url)
            tree = html.fromstring(r.content)

            menu = tree.xpath(
                '//div[@id="{0}-content"]/table[@class="offer"]'
                '/tbody/tr/td[not(@class="weight")]/text()'.format(self.week[day])
            )

            for i in range(0, len(menu), 2):
                dishes.append({'name': menu[i], 'price': menu[i+1]})
            return dishes

        elif rest_id == 18291268:
            url = "http://www.rebelwings.cz/"
            r = requests.get(url)
            tree = html.fromstring(r.content)

            # Stripping weight at the end
            pattern = "\([0-9]+g.*\)$"

            # Week offer
            path = '//div[@class="section dark"][@id="sectionWeeklyMenu"]//div[@class="foodlist"][2]'
            menu = tree.xpath(path + '//div[@class="foodname"]/strong/text()')
            prices = tree.xpath(path + '//div[@class="foodprice"]/text()')

            for name, price in zip(menu, prices):
                name = re.sub(pattern, '', name.strip())
                dishes.append({'name': name.strip(), 'price': price.strip()})

            # Day offer
            path = '//div[@class="section dark"][@id="sectionWeeklyMenu"]//div[@class="foodlist"][{0}]'.format(day+3)
            menu = tree.xpath(path + '//div[@class="foodname"]/strong/text()')
            prices = tree.xpath(path + '//div[@class="foodprice"]/text()')

            for name, price in zip(menu, prices):
                name = re.sub(pattern, '', name.strip())
                dishes.append({'name': name.strip(), 'price': price.strip()})

            return dishes

        elif rest_id == 16506886:
            url = "https://www.hybernia.cz"
            r = requests.get(url)
            tree = html.fromstring(r.content)

            menu = tree.xpath('//div[@class="dailyMenu__content"]//span[@class="dailyMenu__meal-name"]/text()')
            prices = tree.xpath('//div[@class="dailyMenu__content"]//span[@class="dailyMenu__meal-price"]/text()')

            # We do not show the offer of drinks
            for name, price in zip(menu[:-2], prices[:-2]):
                dishes.append({'name': name, 'price': price})

            return dishes

        elif rest_id == 18271176:
            url = "http://www.blackdogs.cz/praha"
            r = requests.get(url)
            tree = html.fromstring(r.content)

            menu = tree.xpath(
                '//div[@class="dailyMenu_item dailyMenu_itemToday"]//span[@class="menu-item-name"]/text()'
            )
            prices = tree.xpath(
                '//div[@class="dailyMenu_item dailyMenu_itemToday"]//span[@class="menu-item-price"]/text()'
            )

            # Stripping and filtering the answer
            menu = self.strip_menu(menu)

            for name, price in zip(menu, prices):
                dishes.append({'name': name, 'price': price})

            return dishes

        elif rest_id == 16510118:
            url = "http://www.kolkovna.cz/cs/kolkovna-celnice-13/denni-menu"
            r = requests.get(url)
            tree = html.fromstring(r.content)

            # Stripping the list of allergens at the end
            pattern = "(,?[0-9]+)+$"

            path = '//div[@class="dailyMenuWeek"][1]/section[{0}]'.format(day+1)
            menu = tree.xpath(path + '//td[@class="name"]/text()')
            prices = tree.xpath(path + '//td[@class="price"]/text()')

            for name, price in zip(menu, prices):
                name = re.sub(pattern, '', name.strip())
                dishes.append({'name': name.strip(), 'price': price})

            return dishes

        elif rest_id == 16517493:
            url = "http://hooters.cz/cz/vodickova/Menu/1"
            r = requests.get(url)
            tree = html.fromstring(r.content)

            path = '//div[@class="menuListBlock"][{0}]/table[@class="menuList"]'

            # The daily menu
            menu = tree.xpath(path.format(day + 1) + '//td/text()')
            sides = tree.xpath(path.format(day + 1) + '//td/span/text()')

            # Stripping and filtering the answer
            menu = self.strip_menu(menu)

            # Creating dishes
            for i in range(0, len(menu), 2):
                dishes.append({'name': menu[i], 'price': menu[i + 1]})

            # Appending side dishes
            for i in range(len(sides)):
                dishes[i + 1]['name'] = dishes[i + 1]['name'] + " " + sides[i]

            return dishes

        elif rest_id == 16506101:
            # Sending URL with image of the menu
            days = ["pondeli", "utery", "streda", "ctvrtek", "patek"]
            url = "http://www.brasserielagare.cz/files/POLEDNI%20MENU/{0}.jpg".format(days[day])
            dishes.append({'name': url, 'price': None})
            return dishes

        elif rest_id == 16506344:
            url = "http://pizzacoloseum.cz/na-porici/denni-menu"
            r = requests.get(url)
            tree = html.fromstring(r.content.replace("<span>", ""))

            menu = tree.xpath('//div[@class="content-cesky-preklad"]/text()')
            prices = tree.xpath('//div[@class="field-cena-content"]/text()')
            allergens = tree.xpath('//div[@class="content-alergeny"]/text()')

            # Creating dishes
            tmp = list()
            for name, allergen, price in zip(menu, allergens, prices):
                tmp.append({'name': name + ", " + allergen, 'price': price})

            # Selecting only the soup of the day and rest of the week menu
            dishes.append(tmp[day])
            for dish in tmp[5:]:
                dishes.append(dish)

            return dishes

        elif rest_id == 16506517:
            url = "http://www.napekarce.cz"
            r = requests.get(url)
            tree = html.fromstring(r.content.replace("<br />", ",  "))

            path = '//table[@class="dailyMenuTable"]'
            weights = tree.xpath(path + '//td[@class="td-cislo"]/text()')
            menu = tree.xpath(path + '//span[@class="td-jidlo-obsah"]/text()')
            prices = tree.xpath(path + '//td[@class="td-cena"]/text()')

            # Stripping and filtering the answer
            menu = self.strip_menu(menu)

            # Creating dishes
            for weight, name, price in zip(weights, menu, prices):
                dishes.append({'name': weight + " - " + name, 'price': price})
            return dishes

        elif rest_id == 16506646:
            url = "https://www.midtowngrill.cz/poledn-menu/"
            dishes.append({'name': url, 'price': None})
            return dishes

        else:
            return dishes
