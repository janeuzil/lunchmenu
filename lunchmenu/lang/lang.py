# coding=utf-8
class Answers(object):
    def __init__(self, lang):
        self.languages = (
            "ar",
            "cs",
            "en",
            "hr",
            "sk"
        )
        if lang == "ar":
            self.help = (
                "Hello <@personEmail:{0}>, would you like to know the lunch menu?\n\n"
                "List of commands:\n\n"
                "- **{1}  &lt;number&gt;** - to add a favourite restaurant to the personal list\n" +
                "- **{2} &lt;number&gt;** - to delete a favourite restaurant from the personal list\n"
                "- **{3}** - to show this help\n"
                "- **{4} &lt;language&gt;** - to set the language\n"
                "- **{5}** - to list your favourite restaurants\n"
                "- **{6} &lt;number&gt;** - to get the lunch menu\n"
                "- **{7} &lt;name&gt;** - to search for a restaurants\n\n"
                "Glossary:\n"
                "- **&lt;argument&gt;** - mandatory argument\n\n"
                "Examples:\n"
                "- **{7} Moe's Tavern** - will display list of restaurants Moe's Tavern and their addresses\n"
                "- **{1} 2** - will add second restaurant from the previous search in the list\n"
                "- **{6} 1** - will show the lunch menu for the restaurant first in your list\n"
                "- **{2} {8}** - will print all the daily menus of your favourite restaurants\n\n"
                "Supported languages:\n"
                "- **ar** - Arabic\n"
                "- **cs** - Czech\n"
                "- **hr** - Croatian\n"
                "- **en** - English\n"
                "- **sk** - Slovak\n"
            )
            self.welcome_direct = (
                "Hello <@personEmail:{0}>, I am the lunch menu bot.\n\n"
                "Type **{1}** for list of commands."
            )
            self.welcome_group = (
                "Hello, I am the lunch menu bot.\n\nType **<@personEmail:{0}> {1}** for list of commands.\n\n"
                "Keep in mind, that this is a group room. I answer only if I am mentioned using **'@'**."
            )
            self.unknown = "I am sorry, I do not understand. Please type **{0}** to get list of commands."
            self.not_found = "I am sorry, but based on your input, no restaurant could be found."
            self.bad_search = (
                "I am sorry, but you must first provide a number based from your previous search result.\n\n"
                "Try to type **{0} &lt;name&gt;** to get the numbered list of restaurants based "
                "on the provided name and then **{1} &lt;number&gt;** to add this restaurant into your favourites."
            )
            self.add_success = (
                "Restaurant successfully added into your favourite list. Type **{0}** to see your list "
                "of favourite restaurants."
            )
            self.list_empty = "No favourite restaurants found, please add at least one before using this command."
            self.bad_param = (
                "I am sorry, but I cannot find selected restaurant. Incorrect number provided "
                "or no matching restaurant in your list of favourites."
            )
            self.del_success = "Restaurant successfully deleted from the list of your favourite restaurants."
            self.lang_set = "Language successfully set. Type **{0}** to see new list of commands in your language."
            self.lang_unsupported = (
                "Cannot determine the language or this language is not supported yet. "
                "Type **{0}** to see the list of supported languages."
            )
            self.no_menu = "I am sorry, but this restaurant does not provide a daily menu today."

        elif lang == "cs":
            self.help = (
                "Dobrý den <@personEmail:{0}>, chcete vědět, co mají dnes dobrého k obědu?\n\n"
                "Seznam příkazů:\n\n"
                "- **{1}  &lt;číslo&gt;** - přidá zařízení na Váš seznam oblíbených restaurací\n" +
                "- **{2} &lt;číslo&gt;** - odebere zařízení z Vašeho seznamu oblíbených restaurací\n"
                "- **{3}** - zobrazí tuto nápovědu\n"
                "- **{4} &lt;jazyk&gt;** - nastaví jazyk\n"
                "- **{5}** - zobrazí seznam Vašich oblíbených restaurací\n"
                "- **{6} &lt;číslo&gt;** - zobrazí denní menu zvolené restaurace\n"
                "- **{7} &lt;název&gt;** - vyhledá seznam restaurací na základě uvedeného názvu\n\n"
                "Vysvětlivky:\n"
                "- **&lt;argument&gt;** - povinný argument\n\n"
                "Příklady:\n"
                "- **{7} U Očka** - zobrazí seznam restaurací s názvem U Očka a jejich adresy\n"
                "- **{1} 2** - přidá druhou restauraci z předchozího hledání na Váš seznam\n"
                "- **{6} 1** - zobrazí denní menu restaurace na druhé pozici ve Vašem seznamu\n"
                "- **{2} {8}** - zobrazí všechna denní menu restaurací z Vašeho seznamu\n\n"
                "Podporované jazyky:\n"
                "- **ar** - Arabština\n"
                "- **cs** - Čeština\n"
                "- **hr** - Chorvatština\n"
                "- **en** - Angličtina\n"
                "- **sk** - Slovenština\n"
            )
            self.unknown = "Omlouvám se, ale nerozumím. Zadejte prosím **{0}** pro seznam příkazů."
            self.not_found = "Omlouvám se, ale na základě zadaného názvu nebyla nalezena žádná restaurace."
            self.bad_search = (
                "Omlouvám se, ale musíte nejprve zadat číslo restaurace na základě minulého hledání.\n\n"
                "Zkuste zadat  **{0} &lt;název&gt;** pro získání číselného seznamu restaurací na základě zadaného "
                "názvu a poté **{1} &lt;číslo&gt;** k přídání zařízení na seznam Vašich oblíbených restaurací."
            )
            self.add_success = (
                "Zařízení bylo úspešně přidáno na seznam oblíbených zařízení. Zadejte **{0}** pro zobrazení seznamu "
                "Vašich oblíbencýh restaurací."
            )
            self.list_empty = (
                "Nebyly nalezeny žádné oblíbené restaurace, prosím přidejte do seznamu alespoň jednu před použítím "
                "tohoto příkazu."
            )
            self.bad_param = (
                "Omlouvám se, ale nemohu najít požadovanou restauraci. Zadáné číslo restaurace neodpovídá žádnému "
                "zařízení z Vašeho seznamu."
            )
            self.del_success = "Zařízení úspěšně odebráno z Vašeho seznamu oblíbených restaurací."
            self.lang_set = (
                "Jazyk úspěšně nastaven. Zadejte **{0}** pro zobrazení nového seznamu příkazů ve Vašem jazyce."
            )
            self.lang_unsupported = (
                "Nemohu rozpoznat jazyk nebo tento jazyk ještě není podporovaný. "
                "Zadejte **{0}** pro zobrazení seznamu podporovaných jazyků."
            )
            self.no_menu = "Omlouvám se, ale tato restaurace dnes nenabízí žádné denní menu."

        elif lang == "en":
            self.help = (
                    "Hello <@personEmail:{0}>, would you like to know the lunch menu?\n\n"
                    "List of commands:\n\n"
                    "- **{1}  &lt;number&gt;** - to add a favourite restaurant to the personal list\n" +
                    "- **{2} &lt;number&gt;** - to delete a favourite restaurant from the personal list\n"
                    "- **{3}** - to show this help\n"
                    "- **{4} &lt;language&gt;** - to set the language\n"
                    "- **{5}** - to list your favourite restaurants\n"
                    "- **{6} &lt;number&gt;** - to get the lunch menu\n"
                    "- **{7} &lt;name&gt;** - to search for a restaurants\n\n"
                    "Glossary:\n"
                    "- **&lt;argument&gt;** - mandatory argument\n\n"
                    "Examples:\n"
                    "- **{7} Moe's Tavern** - will display list of restaurants Moe's Tavern and their addresses\n"
                    "- **{1} 2** - will add second restaurant from the previous search in the list\n"
                    "- **{6} 1** - will show the lunch menu for the restaurant first in your list\n"
                    "- **{2} {8}** - will print all the daily menus of your favourite restaurants\n\n"
                    "Supported languages:\n"
                    "- **ar** - Arabic\n"
                    "- **cs** - Czech\n"
                    "- **hr** - Croatian\n"
                    "- **en** - English\n"
                    "- **sk** - Slovak\n"
            )
            self.welcome_direct = (
                "Hello <@personEmail:{0}>, I am the lunch menu bot.\n\n"
                "Type **{1}** for list of commands."
            )
            self.welcome_group = (
                "Hello, I am the lunch menu bot.\n\nType **<@personEmail:{0}> {1}** for list of commands.\n\n"
                "Keep in mind, that this is a group room. I answer only if I am mentioned using **'@'**."
            )
            self.unknown = "I am sorry, I do not understand. Please type **{0}** to get list of commands."
            self.not_found = "I am sorry, but based on your input, no restaurant could be found."
            self.bad_search = (
                "I am sorry, but you must first provide a number based from your previous search result.\n\n"
                "Try to type **{0} &lt;name&gt;** to get the numbered list of restaurants based "
                "on the provided name and then **{1} &lt;number&gt;** to add this restaurant into your favourites."
            )
            self.add_success = (
                "Restaurant successfully added into your favourite list. Type **{0}** to see your list "
                "of favourite restaurants."
            )
            self.list_empty = "No favourite restaurants found, please add at least one before using this command."
            self.bad_param = (
                "I am sorry, but I cannot find selected restaurant. Incorrect number provided "
                "or no matching restaurant in your list of favourites."
            )
            self.del_success = "Restaurant successfully deleted from the list of your favourite restaurants."
            self.lang_set = "Language successfully set. Type **{0}** to see new list of commands in your language."
            self.lang_unsupported = (
                "Cannot determine the language or this language is not supported yet. "
                "Type **{0}** to see the list of supported languages."
            )
            self.no_menu = "I am sorry, but this restaurant does not provide a daily menu today."

        elif lang == "hr":
            self.help = (
                    "Hello <@personEmail:{0}>, would you like to know the lunch menu?\n\n"
                    "List of commands:\n\n"
                    "- **{1}  &lt;number&gt;** - to add a favourite restaurant to the personal list\n" +
                    "- **{2} &lt;number&gt;** - to delete a favourite restaurant from the personal list\n"
                    "- **{3}** - to show this help\n"
                    "- **{4} &lt;language&gt;** - to set the language\n"
                    "- **{5}** - to list your favourite restaurants\n"
                    "- **{6} &lt;number&gt;** - to get the lunch menu\n"
                    "- **{7} &lt;name&gt;** - to search for a restaurants\n\n"
                    "Glossary:\n"
                    "- **&lt;argument&gt;** - mandatory argument\n\n"
                    "Examples:\n"
                    "- **{7} Moe's Tavern** - will display list of restaurants Moe's Tavern and their addresses\n"
                    "- **{1} 2** - will add second restaurant from the previous search in the list\n"
                    "- **{6} 1** - will show the lunch menu for the restaurant first in your list\n"
                    "- **{2} {8}** - will print all the daily menus of your favourite restaurants\n\n"
                    "Supported languages:\n"
                    "- **ar** - Arabic\n"
                    "- **cs** - Czech\n"
                    "- **hr** - Croatian\n"
                    "- **en** - English\n"
                    "- **sk** - Slovak\n"
            )
            self.welcome_direct = (
                "Hello <@personEmail:{0}>, I am the lunch menu bot.\n\n"
                "Type **{1}** for list of commands."
            )
            self.welcome_group = (
                "Hello, I am the lunch menu bot.\n\nType **<@personEmail:{0}> {1}** for list of commands.\n\n"
                "Keep in mind, that this is a group room. I answer only if I am mentioned using **'@'**."
            )
            self.unknown = "I am sorry, I do not understand. Please type **{0}** to get list of commands."
            self.not_found = "I am sorry, but based on your input, no restaurant could be found."
            self.bad_search = (
                "I am sorry, but you must first provide a number based from your previous search result.\n\n"
                "Try to type **{0} &lt;name&gt;** to get the numbered list of restaurants based "
                "on the provided name and then **{1} &lt;number&gt;** to add this restaurant into your favourites."
            )
            self.add_success = (
                "Restaurant successfully added into your favourite list. Type **{0}** to see your list "
                "of favourite restaurants."
            )
            self.list_empty = "No favourite restaurants found, please add at least one before using this command."
            self.bad_param = (
                "I am sorry, but I cannot find selected restaurant. Incorrect number provided "
                "or no matching restaurant in your list of favourites."
            )
            self.del_success = "Restaurant successfully deleted from the list of your favourite restaurants."
            self.lang_set = "Language successfully set. Type **{0}** to see new list of commands in your language."
            self.lang_unsupported = (
                "Cannot determine the language or this language is not supported yet. "
                "Type **{0}** to see the list of supported languages."
            )
            self.no_menu = "I am sorry, but this restaurant does not provide a daily menu today."

        elif lang == "sk":
            self.help = (
                    "Dobrý den <@personEmail:{0}>, chcete vědět, co mají dnes dobrého k obědu?\n\n"
                    "Seznam příkazů:\n\n"
                    "- **{1}  &lt;číslo&gt;** - přidá zařízení na Váš seznam oblíbených restaurací\n" +
                    "- **{2} &lt;číslo&gt;** - odebere zařízení z Vašeho seznamu oblíbených restaurací\n"
                    "- **{3}** - zobrazí tuto nápovědu\n"
                    "- **{4} &lt;jazyk&gt;** - nastaví jazyk\n"
                    "- **{5}** - zobrazí seznam Vašich oblíbených restaurací\n"
                    "- **{6} &lt;číslo&gt;** - zobrazí denní menu zvolené restaurace\n"
                    "- **{7} &lt;název&gt;** - vyhledá seznam restaurací na základě uvedeného názvu\n\n"
                    "Vysvětlivky:\n"
                    "- **&lt;argument&gt;** - povinný argument\n\n"
                    "Příklady:\n"
                    "- **{7} U Očka** - zobrazí seznam restaurací s názvem U Očka a jejich adresy\n"
                    "- **{1} 2** - přidá druhou restauraci z předchozího hledání na Váš seznam\n"
                    "- **{6} 1** - zobrazí denní menu restaurace na druhé pozici ve Vašem seznamu\n"
                    "- **{2} {8}** - zobrazí všechna denní menu restaurací z Vašeho seznamu\n\n"
                    "Podporované jazyky:\n"
                    "- **ar** - Arabština\n"
                    "- **cs** - Čeština\n"
                    "- **hr** - Chorvatština\n"
                    "- **en** - Angličtina\n"
                    "- **sk** - Slovenština\n"
            )
            self.unknown = "Omlouvám se, ale nerozumím. Zadejte prosím **{0}** pro seznam příkazů."
            self.not_found = "Omlouvám se, ale na základě zadaného názvu nebyla nalezena žádná restaurace."
            self.bad_search = (
                "Omlouvám se, ale musíte nejprve zadat číslo restaurace na základě minulého hledání.\n\n"
                "Zkuste zadat  **{0} &lt;název&gt;** pro získání číselného seznamu restaurací na základě zadaného "
                "názvu a poté **{1} &lt;číslo&gt;** k přídání zařízení na seznam Vašich oblíbených restaurací."
            )
            self.add_success = (
                "Zařízení bylo úspešně přidáno na seznam oblíbených zařízení. Zadejte **{0}** pro zobrazení seznamu "
                "Vašich oblíbencýh restaurací."
            )
            self.list_empty = (
                "Nebyly nalezeny žádné oblíbené restaurace, prosím přidejte do seznamu alespoň jednu před použítím "
                "tohoto příkazu."
            )
            self.bad_param = (
                "Omlouvám se, ale nemohu najít požadovanou restauraci. Zadáné číslo restaurace neodpovídá žádnému "
                "zařízení z Vašeho seznamu."
            )
            self.del_success = "Zařízení úspěšně odebráno z Vašeho seznamu oblíbených restaurací."
            self.lang_set = (
                "Jazyk úspěšně nastaven. Zadejte **{0}** pro zobrazení nového seznamu příkazů ve Vašem jazyce."
            )
            self.lang_unsupported = (
                "Nemohu rozpoznat jazyk nebo tento jazyk ještě není podporovaný. "
                "Zadejte **{0}** pro zobrazení seznamu podporovaných jazyků."
            )
            self.no_menu = "Omlouvám se, ale tato restaurace dnes nenabízí žádné denní menu."

        else:
            raise LangError("Unsupported language - {0}.".format(lang))

    def check_lang(self, lang):
        if lang in self.languages:
            return True
        else:
            return False


class Commands(object):
    def __init__(self, lang):
        if lang == "ar":
            self.add = "add"
            self.all = "all"
            self.delete = "delete"
            self.help = "help"
            self.lang = "lang"
            self.list = "list"
            self.menu = "menu"
            self.search = "search"

        elif lang == "cs":
            self.add = "pridat"
            self.all = "vse"
            self.delete = "odebrat"
            self.help = "pomoc"
            self.lang = "jazyk"
            self.list = "seznam"
            self.menu = "menu"
            self.search = "hledat"

        elif lang == "en":
            self.add = "add"
            self.all = "all"
            self.delete = "delete"
            self.help = "help"
            self.lang = "lang"
            self.list = "list"
            self.menu = "menu"
            self.search = "search"

        elif lang == "hr":
            self.add = "add"
            self.all = "all"
            self.delete = "delete"
            self.help = "help"
            self.lang = "lang"
            self.list = "list"
            self.menu = "menu"
            self.search = "search"

        elif lang == "sk":
            self.add = "add"
            self.all = "all"
            self.delete = "delete"
            self.help = "help"
            self.lang = "lang"
            self.list = "list"
            self.menu = "menu"
            self.search = "search"

        else:
            raise LangError("Unsupported language - {0}.".format(lang))


class LangError(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return repr(self.msg)
