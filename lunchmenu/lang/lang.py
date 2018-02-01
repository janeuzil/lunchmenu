# coding=utf-8
class Answers(object):
    def __init__(self, lang):
        self.languages = (
            "cs",
            "en",
            "hr",
            "pl",
            "sk",
            "tr"
        )

        if lang == "cs":
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
                "- **{6} {8}** - zobrazí všechna denní menu restaurací z Vašeho seznamu\n\n"
                "Podporované jazyky:\n"
                "- **cs** - čeština\n"
                "- **hr** - chorvatština\n"
                "- **en** - angličtina\n"
                "- **pl** - polština\n"
                "- **sk** - slovenština\n"
                "- **tr** - turečtina\n"
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
                    "- **{6} {8}** - will print all the daily menus of your favourite restaurants\n\n"
                    "Supported languages:\n"
                    "- **cs** - Czech\n"
                    "- **hr** - Croatian\n"
                    "- **en** - English\n"
                    "- **pl** - Polish\n"
                    "- **sk** - Slovak\n"
                    "- **tr** - Turkish\n"
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
                    "- **{6} {8}** - will print all the daily menus of your favourite restaurants\n\n"
                    "Supported languages:\n"
                    "- **cs** - Czech\n"
                    "- **hr** - Croatian\n"
                    "- **en** - English\n"
                    "- **pl** - Polish\n"
                    "- **sk** - Slovak\n"
                    "- **tr** - Turkish\n"
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

        elif lang == "pl":
            self.help = (
                    "Witaj <@personEmail:{0}>, czy chciałbyś poznać menu lunchowe?\n\n"
                    "Lista poleceń:\n\n"
                    "- **{1}  &lt;numer&gt;** - dodanie ulubionej restauracji do osobistej listy\n" +
                    "- **{2} &lt;numer&gt;** - usuwanie ulubionej restauracji z osobistej listy\n"
                    "- **{3}** - wyświetlenie tej pomocy\n"
                    "- **{4} &lt;język&gt;** - zmiana języka\n"
                    "- **{5}** - wyświetlenie listy Twoich ulubionych restauracji\n"
                    "- **{6} &lt;numer&gt;** - wyświetlenie menu lunchowego\n"
                    "- **{7} &lt;imię&gt;** - wyszukanie restauracji\n\n"
                    "Słownik:\n"
                    "- **&lt;argument&gt;** - wymagany argument\n\n"
                    "Przykłady:\n"
                    "- **{7} Moe's Tavern** - wyświetlenie listy restauracji Moe's Tavern i ich adresów\n"
                    "- **{1} 2** - dodanie drugiej restauracji z wyników wyszukiwania do listy ulubionych restauracji\n"
                    "- **{6} 1** - wyświetlenie menu lunchowego pierwszej restauracji z listy ulubionych restauracji\n"
                    "- **{6} {8}** - wyświetlenie menu lunchowych wszystkich restauracji z listy\n\n"
                    "Obsługiwane języki:\n"
                    "- **cs** - czeski\n"
                    "- **hr** - chorwacki\n"
                    "- **en** - angielski\n"
                    "- **pl** - polski\n"
                    "- **sk** - słowacki\n"
                    "- **tr** - turecki\n"
            )
            self.unknown = "Wybacz, nie rozumiem. Wpisz **{0}** aby wyświetlić listę komend."
            self.not_found = "Wybacz, nie znaleziono żadnych restauracji pasujących do Twojego zapytania."
            self.bad_search = (
                "Wybacz, najpierw musisz podać liczbę z poprzedniego wyszukiwania.\n\n"
                "Spróbuj wpisać **{0} &lt;name&gt;** aby uzyskać ponumerowaną listę restauracji "
                "na podstawię podanej nazwy, a następnie **{1} &lt;number&gt;** aby dodać restaurację "
                "do listy Twoich ulubionych restauracji."
            )
            self.add_success = (
                "Restautacja została dodana do Twojej listy. Wpisz **{0}** aby zobaczyś swoją listę "
                "ulubionych restauracji."
            )
            self.list_empty = (
                "Nie znaleziono żadnych ulubionych restautacji, dodaj przynajmniej "
                "jedną przed wpisaniem tej komendy."
            )
            self.bad_param = (
                "Wybacz, nie mogę znaleźć wybranej restauracji. Podano niepoprawną liczbę,"
                "lub pasującej restauracji w liście ulubionych restauracji."
            )
            self.del_success = "Restauracja pomyślnie usunięta z listy ulub ionych restauracji."
            self.lang_set = "Język pomyślnie wybrany. Wpisz **{0}** by zobaczyć nową listę komend w Twoim języku."
            self.lang_unsupported = (
                "Nie można określić języka, lub wybrany język nie jest wspierany."
                "Wpisz **{0}** aby zpbaczyć listę wspieranych języków."
            )
            self.no_menu = "Wybacz, ta restauracjia nie udostępniła dzisiaj swojego dziennego menu."

        elif lang == "sk":
            self.help = (
                    "Dobrý deň <@personEmail:{0}>, chcete vediet, čo majú dnes dobré na obed?\n\n"
                    "Zoznam príkazov:\n\n"
                    "- **{1}  &lt;číslo&gt;** - pridá zariadenie na Váš zoznam obľúbených reštaurácií\n" +
                    "- **{2} &lt;číslo&gt;** - odoberie zariadenie z Vášho zoznamu obľúbených reštaurácií\n"
                    "- **{3}** - zobrazí túto nápovedu\n"
                    "- **{4} &lt;jazyk&gt;** - nastaví jazyk\n"
                    "- **{5}** - zobrazí zoznam Vaších obľúbených reštaurácií\n"
                    "- **{6} &lt;číslo&gt;** - zobrazí denné menu zvolenej reštaurácie\n"
                    "- **{7} &lt;názov&gt;** - vyhľadá zoznam reštaurácií na základe uvedeného názvu\n\n"
                    "Vysvetlivky:\n"
                    "- **&lt;argument&gt;** - povinný argument\n\n"
                    "Príklady:\n"
                    "- **{7} U Očka** - zobrazí zoznam reštaurácií s názvom U Očka a ich adresy\n"
                    "- **{1} 2** - pridá druhú reštauráciu z predchádzajúceho hľadania na Váš zoznam\n"
                    "- **{6} 1** - zobrazí denné menu reštaurácie na druhej pozícií vo Vašom zozname\n"
                    "- **{6} {8}** - zobrazí všetky denné menu reštaurácií z Vášho zoznamu\n\n"
                    "Podporované jazyky:\n"
                    "- **cs** - čeština\n"
                    "- **hr** - chorvátčina\n"
                    "- **en** - angličtina\n"
                    "- **pl** - polština\n"
                    "- **sk** - slovenčina\n"
                    "- **tr** - turečtina\n"
            )
            self.unknown = "Ospravedlňujem sa, ale nerozumiem. Zadajte prosím **{0}** pre zoznam príkazov."
            self.not_found = "Je mi to ľúto, ale na základe zadaného názvu nebola nájdená žiadna reštaurácia."
            self.bad_search = (
                "Ospravedlňujem sa, ale musíte nejskôr zadať číslo reštaurácie na základe minulého hľadania.\n\n"
                "Skúste zadať  **{0} &lt;názov&gt;** pre získanie číselného zoznamu reštaurácie na základe zadaného "
                "názvu a potom **{1} &lt;číslo&gt;** k pridaniu zariadenia na zoznam Vašich obľúbených reštaurácií."
            )
            self.add_success = (
                "Stravovacie zariadenie bolo úspešne pridané do zoznamu obľúbených reštaurácií. Zadajte **{0}** pre zobrazenie zoznamu "
                "Vašich obľúbených reštaurácií."
            )
            self.list_empty = (
                "Neboli nájdené žiadne obľúbené reštaurácie, prosím pridajte do zoznamu aspoň jednu pred použitím tohoto príkazu."
            )
            self.bad_param = (
                "Je mi to ľúto, ale nemôžem nájsť požadovanú reštauráciu. Zadané číslo reštaurácie nezodpovedá žiadnemu "
                "zariadeniu z Vášho zoznamu."
            )
            self.del_success = "Reštaurácia úspešne odstránená z Vášho zoznamu obľúbených reštaurácií."
            self.lang_set = (
                "Jazyk bol úspešne nastavený. Zadajte **{0}** pre zobrazenie nového zoznamu príkazov vo Vašom jazyku."
            )
            self.lang_unsupported = (
                "Nemôžem rozpoznať zvolený jazyk alebo jazyk ešte nie je podporovaný. "
                "Zadajte **{0}** pre zobrazenie zoznamu podporovaných jazykov."
            )
            self.no_menu = "Ospravedlňujem sa, ale táto reštaurácia dnes neponúka žiadne denné menu."

        elif lang == "tr":
            self.help = (
                    "Merhaba <@personEmail:{0}>, oğlen menüsünü öğrenmek ister misiniz?\n\n"
                    "Komut listesi:\n\n"
                    "- **{1}  &lt;sayı&gt;** - Beğendiğiniz restoranları kişisel listenize ekleyin\n" +
                    "- **{2} &lt;sayı&gt;** - Restoranları kişisel listenizden silin\n"
                    "- **{3}** - Neler yapabileceğimi görün\n"
                    "- **{4} &lt;dil&gt;** - Dili değiştirin\n"
                    "- **{5}** - Kişisel restoran listenizi görüntüleyin\n"
                    "- **{6} &lt;sayı&gt;** - Ögle menüsünü oğrenin\n"
                    "- **{7} &lt;isim&gt;** - Restoranları arayın\n\n"
                    "Terimler:\n"
                    "- **&lt;terim&gt;** - Zorunlu terimler\n\n"
                    "Örnekler:\n"
                    "- **{7} Moe's Tavern** - Moe's Tavern isimli restoranları ve adreslerini gösterir\n"
                    "- **{1} 2** - Arama listesindeki ikinci restoranı kişisel listenize ekler\n"
                    "- **{6} 1** - Kişisel listenizdeki ilk restoranın öğle menüsünü gösterir\n"
                    "- **{6} {8}** - Kişisel listenizdeki tüm restoranların öğle menüsünü gösterir\n\n"
                    "Desteklenen diller:\n"
                    "- **ar** - Arapça\n"
                    "- **cs** - Çekçe\n"
                    "- **hr** - Hırvatça\n"
                    "- **en** - İngilizce\n"
                    "- **pl** - Polonya\n"
                    "- **sk** - Slovakça\n"
                    "- **tr** - Türk\n"
            )
            self.unknown = "Üzgünüm, anlayamadım. **{0}** yazarak tüm komutları görüntüleyin."
            self.not_found = "Üzgünüm, aradığınız restoran bulunamadı."
            self.bad_search = (
                "Öncelikle az önceki aramanıza göre bir sayı belirtin.\n\n"
                "**{0} &lt;isim&gt;** yazarak restoranların listesini görüntüleyin. "
                "Belirtilen isim ve **{1} &lt;number&gt;** restoranı restoran listenize ekler."
            )
            self.add_success = (
                "Restoran başarıyla listenize eklendi. **{0}** yazarak en sevdiğiniz restoranları görüntüleyin."
            )
            self.list_empty = "Favori restoranlarınız bulunamadı. Önce listenize restoranları ekleyin."
            self.bad_param = (
                "Üzgünüm, aradığınız restoran numarası bulunamadı. Sayı veya restoran ismi yanlış."
            )
            self.del_success = "Restoran başarıyla listenizden silindi."
            self.lang_set = "Dil ayarı başarıyla değiştirildi. **{0}** yazarak dilinizdeki komutları görüntüleyin."
            self.lang_unsupported = (
                "Dil algılanamadı veya bu henüz desteklenmeyen bir dil. "
                "**{0}** yazarak desteklenen tüm dilleri görüntüleyin."
            )
            self.no_menu = "Üzgünüm, aradığınız restoran bugün öğle menüsü sunmamaktadır."

        else:
            raise LangError("Unsupported language - {0}.".format(lang))

    def check_lang(self, lang):
        if lang in self.languages:
            return True
        else:
            return False


class Commands(object):
    def __init__(self, lang):
        if lang == "cs":
            self.add = "pridej"
            self.all = "vse"
            self.delete = "smaz"
            self.help = "pomoc"
            self.lang = "jazyk"
            self.list = "seznam"
            self.menu = "menu"
            self.search = "hledej"

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

        elif lang == "pl":
            self.add = "dodaj"
            self.all = "wszystkie"
            self.delete = "usun"
            self.help = "pomoc"
            self.lang = "jezyk"
            self.list = "lista"
            self.menu = "menu"
            self.search = "wyszukaj"

        elif lang == "sk":
            self.add = "pridaj"
            self.all = "vsetko"
            self.delete = "zmaz"
            self.help = "pomoc"
            self.lang = "jazyk"
            self.list = "zoznam"
            self.menu = "menu"
            self.search = "hladaj"

        elif lang == "tr":
            self.add = "ekle"
            self.all = "hepsi"
            self.delete = "sil"
            self.help = "yardim"
            self.lang = "dil"
            self.list = "liste"
            self.menu = "menu"
            self.search = "ara"

        else:
            raise LangError("Unsupported language - {0}.".format(lang))


class LangError(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return repr(self.msg)
