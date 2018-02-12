# encoding: utf-8
from __future__ import unicode_literals


class Answers(object):
    def __init__(self, lang):
        self.languages = (
            "cz",
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
                "- **{6} [číslo]** - zobrazí denní menu zvolené restaurace\n"
                "- **{7} &lt;název&gt;** - vyhledá seznam restaurací na základě uvedeného názvu\n\n"
                "Vysvětlivky:\n"
                "- **&lt;argument&gt;** - povinný argument\n"
                "- **[argument]** - volitelný argument\n\n"
                "Příklady:\n"
                "- **{7} U Očka** - zobrazí seznam restaurací s názvem U Očka a jejich adresy\n"
                "- **{1} 2** - přidá druhou restauraci z předchozího hledání na Váš seznam\n"
                "- **{6} 1** - zobrazí denní menu restaurace na druhé pozici ve Vašem seznamu\n"
                "- **{6}** - zobrazí všechna denní menu restaurací z Vašeho seznamu\n\n"
                "Podporované jazyky:\n"
                "- **cz** - čeština\n"
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
                "Vašich oblíbených restaurací."
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
            self.no_time = (
                "Nebyl specifikovaný žádný, správný či obědový čas, tudíž předpokládám "
                "Váš dnešní oběd na nejbližší celou hodinu."
            )
            self.vote_success = (
                "Hlas úspěšně zaregistrován, seznam s kolegyněmi a kolegy, kteří projeví stejný zájem Vám bude zaslán "
                "15 minut před plánovaným obědem."
            )
            self.vote_late = "Omlouvám se, ale pro dnešní den je již hlasování ukončeno. Zkuste to prosím zítra."
            self.no_votes = "Omlouvám se, ale nikdo neprojevil zájem jít dnes do této restaurace."

        elif lang == "en":
            self.help = (
                    "Hello <@personEmail:{0}>, would you like to know the lunch menu?\n\n"
                    "List of commands:\n\n"
                    "- **{1}  &lt;number&gt;** - to add a favourite restaurant to the personal list\n" +
                    "- **{2} &lt;number&gt;** - to delete a favourite restaurant from the personal list\n"
                    "- **{3}** - to show this help\n"
                    "- **{4} &lt;language&gt;** - to set the language\n"
                    "- **{5}** - to list your favourite restaurants\n"
                    "- **{6} [number]** - to get the lunch menu of a given restaurant\n"
                    "- **{7} &lt;name&gt;** - to search for a restaurants\n"
                    "- **{8} &lt;number&gt; [time]** - to vote for a restaurant of a day at the given time\n\n"
                    "Glossary:\n"
                    "- **&lt;argument&gt;** - mandatory argument\n"
                    "- **[argument]** - optional argument\n\n"
                    "Examples:\n"
                    "- **{7} Moe's Tavern** - will display list of restaurants Moe's Tavern and their addresses\n"
                    "- **{1} 2** - will add second restaurant from the previous search in the list\n"
                    "- **{6} 1** - will show the lunch menu for the restaurant first in your list\n"
                    "- **{6}** - will print all the daily menus of your favourite restaurants\n"
                    "- **{8} 1 12:30** - will set the today's vote for the first restaurant in your list at 12:30\n\n"
                    "Supported languages:\n"
                    "- **cz** - Czech\n"
                    "- **hr** - Croatian\n"
                    "- **en** - English\n"
                    "- **pl** - Polish\n"
                    "- **sk** - Slovak\n"
                    "- **tr** - Turkish\n"
            )
            self.welcome_direct = (
                "Hello <@personEmail:{0}>, I am the lunch menu bot.\n\n"
                "I help to find the daily lunch menu in your favourite restaurants. How do I work?\n\n"
                "Let's say that you often go to restaurant **Good Food** for the lunch. You type **{1} Good Food** "
                "to search for it, because there might be another one with the same name. After you will get "
                "a numbered list of results from previous search, you might see that the second **Good Food** "
                "restaurant at given address is the one you desired. Type **{2} 2** to add this second result to your "
                "preferred list of restaurants. To see your list of favourites, type **{3}**. Now simply ask the bot "
                "what is the menu in all restaurants using **{4}** command.\n\n"
                "Do you often go for a lunch alone? Just type **{5} 2 12:30** and 15 minutes before the actual lunch "
                "you will receive a list of colleagues and their intended time to go in the same chosen restaurant. "
                "Afterwards, you can simply Spark them and join your colleagues for a great collaborative lunch.\n\n"
                "If you need any help, change language or see the list of commands, type **{6}** in this Spark room."
            )
            self.welcome_group = (
                "Hello, I am the lunch menu bot.\n\n"
                "I help to find the daily lunch menu in your favourite restaurants. How do I work?\n\n"
                "Let's say that you often go to restaurant **Good Food** for the lunch. "
                "You type **<@personEmail:{0}> {1} Good Food** to search for it, because there might be another "
                "one with the same name. After you will get a numbered list of results from previous search, "
                "you might see that the second **Good Food** restaurant at given address is the one you desired. "
                "Type **<@personEmail:{0}> {2} 2** to add this second result to your preferred list of restaurants. "
                "To see your list of favourites, type **<@personEmail:{0}> {3}**. Now simply ask the bot "
                "what is the menu in all restaurants using **{4}** command.\n\n"
                "Do you often go for a lunch alone? Just type **{5} 2 12:30** and 15 minutes before the actual lunch "
                "you will receive a list of colleagues and their intended time to go in the same chosen restaurant. "
                "Afterwards, you can simply Spark them and join your colleagues for a great collaborative lunch.\n\n"
                "If you need any help, change language or see the list of commands, "
                "type **<@personEmail:{0}> {6}** in this Spark room.\n\n"
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
            self.no_time = "No time, past time or incorrect one was specified, assuming lunch time at the closest hour."
            self.vote_success = (
                "Vote successfully registered, the list of colleagues with the same intent"
                " will be sent prior to your scheduled time."
            )
            self.vote_late = "I am sorry, but it is too late to vote. Try it tomorrow."
            self.no_votes = "I am sorry, but no one has the intention to go into this restaurant today."

        elif lang == "hr":
            self.help = (
                    "Bok <@personEmail:{0}>, želiš li znati dnevni meni?\n\n"
                    "Lista naredbi:\n\n"
                    "- **{1}  &lt;number&gt;** - za dodavanje omiljenog restorana u personaliziranu listu\n" +
                    "- **{2} &lt;number&gt;** - za brisanje restorana iz personalizirane liste\n"
                    "- **{3}** - za prikaz pomoći\n"
                    "- **{4} &lt;language&gt;** - za postavljanje jezika\n"
                    "- **{5}** - za ispis tvojih omiljenih restorana\n"
                    "- **{6} [number]** - za prikaz dnevnog menija\n"
                    "- **{7} &lt;name&gt;** - za pretragu restorana\n\n"
                    "Glosar:\n"
                    "- **&lt;argument&gt;** - obavezni argument\n"
                    "- **[argument]** - neobavezni argument\n\n"
                    "Primjeri:\n"
                    "- **{7} Mrzla Piva** - će ispisati sve restorane s imenom Mrzla Piva i njihove adrese\n"
                    "- **{1} 2** - će dodati restoran pod rednim brojem 2 iz prethodne pretrage\n"
                    "- **{6} 1** - će prikazati dnevni meni za prvi restoran u tvojoj listi\n"
                    "- **{6}** - će ispisati sve dnevne menije tvojih omiljenih restorana\n\n"
                    "Podržani jezici:\n"
                    "- **cz** - Češki\n"
                    "- **hr** - Hrvatski\n"
                    "- **en** - Engleski\n"
                    "- **pl** - Polirati\n"
                    "- **sk** - Slovački\n"
                    "- **tr** - Turski"
            )
            self.unknown = "Oprosti, ne razumijem. Molim te utipkaj **{0}** za listu naredbi."
            self.not_found = "Oprosti, ali za tvoj unos ni jedan restoran nije pronađen."
            self.bad_search = (
                "Oprosti, ali najprije moraš odabrati broj iz rezultata pretrage.\n\n"
                "Pokušaj utipkati **{0} &lt;name&gt;** za prikaz numerirane liste restorana temeljen "
                "na imenu i tada **{1} &lt;number&gt;** kako bi taj restoran dodao u listu svojih omiljenih restorana."
            )
            self.add_success = (
                "Restran je uspješno dodan u tvoju listu omiljenih restorana. Utipkaj **{0}** za pregled liste "
                "omiljenih restorana."
            )
            self.list_empty = (
                "Nisu nađeni restorani u listi omiljenih, molim te dodaj barem jedan restoran u listu "
                "omiljenih prije korištenja ove naredbe."
            )
            self.bad_param = (
                "Oprosti, ali ne mogu naći odabrani restoran, utipkan je pogrešan broj "
                "ili ne postoji podudarajući restoran u tvojoj listi."
            )
            self.del_success = "Restoran uspješno izbrisan iz liste tvojih omiljenih restorana."
            self.lang_set = "Jezik uspješno promijenjen. Utipkaj **{0}** za prikaz liste naredbi na tvom jeziku."
            self.lang_unsupported = (
                "Ne mogu utvrditi jezik ili taj jezik nije podržan. "
                "Utipkaj **{0}** za listu podržanih jezika."
            )
            self.no_menu = "Oprosti, ali ovaj restoran ne nudi dnevni meni za danas."
            self.no_time = (
                "Vrijeme nije uneseno, uneseno je vrijeme iz prošlosti ili je vrijeme pogrešno upisano. "
                "Zabilježit ću vrijeme najbližeg sata."
            )
            self.vote_success = (
                "Glas je uspješno registriran, popis kolega sa istom namjerom"
                " biti će poslan prije zabilježenog vremena."
            )
            self.vote_late = "Oprosti, prekasno je za glasanje. Pokušaj sutra."
            self.no_votes = "Oprosti, ali nitko od kolega nema namjeru ići u taj restoran danas."

        elif lang == "pl":
            self.help = (
                    "Witaj <@personEmail:{0}>, czy chciałbyś poznać menu lunchowe?\n\n"
                    "Lista poleceń:\n\n"
                    "- **{1}  &lt;numer&gt;** - dodanie ulubionej restauracji do osobistej listy\n" +
                    "- **{2} &lt;numer&gt;** - usuwanie ulubionej restauracji z osobistej listy\n"
                    "- **{3}** - wyświetlenie tej pomocy\n"
                    "- **{4} &lt;język&gt;** - zmiana języka\n"
                    "- **{5}** - wyświetlenie listy Twoich ulubionych restauracji\n"
                    "- **{6} [numer]** - wyświetlenie menu lunchowego\n"
                    "- **{7} &lt;imię&gt;** - wyszukanie restauracji\n\n"
                    "Słownik:\n"
                    "- **&lt;argument&gt;** - wymagany argument\n"
                    "- **[argument]** - fakultatywny argument\n\n"
                    "Przykłady:\n"
                    "- **{7} Moe's Tavern** - wyświetlenie listy restauracji Moe's Tavern i ich adresów\n"
                    "- **{1} 2** - dodanie drugiej restauracji z wyników wyszukiwania do listy ulubionych restauracji\n"
                    "- **{6} 1** - wyświetlenie menu lunchowego pierwszej restauracji z listy ulubionych restauracji\n"
                    "- **{6}** - wyświetlenie menu lunchowych wszystkich restauracji z listy\n\n"
                    "Obsługiwane języki:\n"
                    "- **cz** - czeski\n"
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
            self.no_time = "Nie podano czasu, lub podano niepoprawny czas zakładając lunch w ciągu następnej godziny."
            self.vote_success = (
                "Głos został zarejestrowany, lista pracowników zamierzających udać się do tej samej restauracji "
                " zostanie przesłana przed zaplanowaną godziną."
            )
            self.vote_late = "Wybacz, ale jest już za późno na głosowanie. Spróbuj jutro."
            self.no_votes = "Wybacz, ale nikt nie wybiera się dziś do tej restauracji."

        elif lang == "sk":
            self.help = (
                    "Dobrý deň <@personEmail:{0}>, chcete vediet, čo majú dnes dobré na obed?\n\n"
                    "Zoznam príkazov:\n\n"
                    "- **{1}  &lt;číslo&gt;** - pridá zariadenie na Váš zoznam obľúbených reštaurácií\n" +
                    "- **{2} &lt;číslo&gt;** - odoberie zariadenie z Vášho zoznamu obľúbených reštaurácií\n"
                    "- **{3}** - zobrazí túto nápovedu\n"
                    "- **{4} &lt;jazyk&gt;** - nastaví jazyk\n"
                    "- **{5}** - zobrazí zoznam Vaších obľúbených reštaurácií\n"
                    "- **{6} [číslo]** - zobrazí denné menu zvolenej reštaurácie\n"
                    "- **{7} &lt;názov&gt;** - vyhľadá zoznam reštaurácií na základe uvedeného názvu\n\n"
                    "Vysvetlivky:\n"
                    "- **&lt;argument&gt;** - povinný argument\n"
                    "- **[argument]** - voliteľný argument\n"
                    "Príklady:\n"
                    "- **{7} U Očka** - zobrazí zoznam reštaurácií s názvom U Očka a ich adresy\n"
                    "- **{1} 2** - pridá druhú reštauráciu z predchádzajúceho hľadania na Váš zoznam\n"
                    "- **{6} 1** - zobrazí denné menu reštaurácie na druhej pozícií vo Vašom zozname\n"
                    "- **{6}** - zobrazí všetky denné menu reštaurácií z Vášho zoznamu\n\n"
                    "Podporované jazyky:\n"
                    "- **cz** - čeština\n"
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
                "Stravovacie zariadenie bolo úspešne pridané do zoznamu obľúbených reštaurácií. "
                "Zadajte **{0}** pre zobrazenie zoznamu Vašich obľúbených reštaurácií."
            )
            self.list_empty = (
                "Neboli nájdené žiadne obľúbené reštaurácie, prosím pridajte do zoznamu aspoň jednu "
                "pred použitím tohoto príkazu."
            )
            self.bad_param = (
                "Je mi to ľúto, ale nemôžem nájsť požadovanú reštauráciu. Zadané číslo reštaurácie "
                "nezodpovedá žiadnemu zariadeniu z Vášho zoznamu."
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
            self.no_time = (
                "Bol zadaný nesprávny, minulý alebo žiadny čas. Predpokladám čas obedu na najbližšiu celú hodinu."
            )
            self.vote_success = (
                "Voľba bola úspešne zaregistrovaná, zoznam kolegov s rovnakým záujomom Vám bude zaslaný "
                "15 minút pred plánovaným obedom."
            )
            self.vote_late = "Ospravedlňujem sa, ale dnešný čas na hlasovanie už vypršal. Skúste to prosím zajtra."
            self.no_votes = "Ospravedlňujem sa, ale žiadny z kolegov nemal dnes záujem o túto reštauráciu."

        elif lang == "tr":
            self.help = (
                    "Merhaba <@personEmail:{0}>, oğlen menüsünü öğrenmek ister misiniz?\n\n"
                    "Komut listesi:\n\n"
                    "- **{1}  &lt;sayı&gt;** - Beğendiğiniz restoranları kişisel listenize ekleyin\n" +
                    "- **{2} &lt;sayı&gt;** - Restoranları kişisel listenizden silin\n"
                    "- **{3}** - Neler yapabileceğimi görün\n"
                    "- **{4} &lt;dil&gt;** - Dili değiştirin\n"
                    "- **{5}** - Kişisel restoran listenizi görüntüleyin\n"
                    "- **{6} [sayı]** - Ögle menüsünü oğrenin\n"
                    "- **{7} &lt;isim&gt;** - Restoranları arayın\n\n"
                    "Terimler:\n"
                    "- **&lt;terim&gt;** - Zorunlu terimler\n"
                    "- **[terim]** - Isteğe bağlı terimler\n\n"
                    "Örnekler:\n"
                    "- **{7} Moe's Tavern** - Moe's Tavern isimli restoranları ve adreslerini gösterir\n"
                    "- **{1} 2** - Arama listesindeki ikinci restoranı kişisel listenize ekler\n"
                    "- **{6} 1** - Kişisel listenizdeki ilk restoranın öğle menüsünü gösterir\n"
                    "- **{6}** - Kişisel listenizdeki tüm restoranların öğle menüsünü gösterir\n\n"
                    "Desteklenen diller:\n"
                    "- **cz** - Çekçe\n"
                    "- **hr** - Hırvatça\n"
                    "- **en** - İngilizce\n"
                    "- **pl** - Lehçe\n"
                    "- **sk** - Slovakça\n"
                    "- **tr** - Türkçe\n"
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
            self.no_time = "Geçmiş veya geçersiz bir saat belirttiniz."
            self.vote_success = (
                "Oyunuz başarıyla alındı. Sizinle aynı seçimi yapan kişiler "
                "belirttiğiniz zamandan önce gönderilecektir."
            )
            self.vote_late = "Oylama için geç kaldınız, lütfen yarın tekrar deneyin."
            self.no_votes = "Maalesef bugün sizinle aynı restorana gitmek isteyen kimse yok."

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
            self.delete = "smaz"
            self.help = "pomoc"
            self.lang = "jazyk"
            self.list = "seznam"
            self.menu = "menu"
            self.search = "hledej"
            self.vote = "hlasuj"

        elif lang == "en":
            self.add = "add"
            self.delete = "delete"
            self.help = "help"
            self.lang = "lang"
            self.list = "list"
            self.menu = "menu"
            self.search = "search"
            self.vote = "vote"

        elif lang == "hr":
            self.add = "dodaj"
            self.delete = "izbrisi"
            self.help = "pomoc"
            self.lang = "jezik"
            self.list = "lista"
            self.menu = "meni"
            self.search = "pretraga"
            self.vote = "glasaj"

        elif lang == "pl":
            self.add = "dodaj"
            self.delete = "usun"
            self.help = "pomoc"
            self.lang = "jezyk"
            self.list = "lista"
            self.menu = "menu"
            self.search = "wyszukaj"
            self.vote = "glosuj"

        elif lang == "sk":
            self.add = "pridaj"
            self.delete = "zmaz"
            self.help = "pomoc"
            self.lang = "jazyk"
            self.list = "zoznam"
            self.menu = "menu"
            self.search = "hladaj"
            self.vote = "hlasuj"

        elif lang == "tr":
            self.add = "ekle"
            self.delete = "sil"
            self.help = "yardim"
            self.lang = "dil"
            self.list = "liste"
            self.menu = "menu"
            self.search = "ara"
            self.vote = "oyla"

        else:
            raise LangError("ERROR: Unsupported language - {0}.".format(lang))


class LangError(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return repr(self.msg)
