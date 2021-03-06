# encoding: utf-8
from __future__ import unicode_literals


class Answers(object):
    def __init__(self, lang):
        self.languages = (
            "cz",
            "en",
            "hr",
            "pl",
            "ru",
            "sk",
            "tr"
        )

        if lang == "cs":
            self.help = (
                "Dobrý den **{0}**, chcete vědět, co mají dnes dobrého k obědu?\n\n"
                "Seznam příkazů:\n\n"
                "- **{1}  &lt;číslo&gt;** - přidá zařízení na Váš seznam oblíbených restaurací\n" +
                "- **{2} &lt;číslo&gt;** - odebere zařízení z Vašeho seznamu oblíbených restaurací\n"
                "- **{3}** - zobrazí tuto nápovědu\n"
                "- **{4} &lt;město&gt;** - nastaví město či oblast pro hledání, výchozí je Praha\n"
                "- **{5} &lt;jazyk&gt;** - nastaví jazyk\n"
                "- **{6}** - zobrazí seznam Vašich oblíbených restaurací\n"
                "- **{7} [číslo]** - zobrazí denní menu zvolené restaurace\n"
                "- **{8} [čas]** - nastaví nebo vypne posílání denního menu každý den v určitém čase\n"
                "- **{9} &lt;název&gt;** - vyhledá seznam restaurací na základě uvedeného názvu\n"
                "- **{10} &lt;číslo&gt; [čas]** - vyjádří Váš zájem jít dnes do dané restaurace v uvedený čas\n\n"
                "Vysvětlivky:\n"
                "- **&lt;argument&gt;** - povinný argument\n"
                "- **[argument]** - volitelný argument\n\n"
                "Příklady:\n"
                "- **{9} U Očka** - zobrazí seznam restaurací s názvem U Očka a jejich adresy\n"
                "- **{1} 2** - přidá druhou restauraci z předchozího hledání na Váš seznam\n"
                "- **{7} 1** - zobrazí denní menu restaurace na druhé pozici ve Vašem seznamu\n"
                "- **{7}** - zobrazí všechna denní menu restaurací z Vašeho seznamu\n"
                "Podporované jazyky:\n"
                "- **cz** - čeština\n"
                "- **hr** - chorvatština\n"
                "- **en** - angličtina\n"
                "- **pl** - polština\n"
                "- **ru** - ruština\n"
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
            self.city_set = "Oblast pro hledání restaurací byla úspěšně nastavena na město {0}."
            self.city_unknown = (
                "Omlouvám se, ale dotazované město nemohu naleznout. "
                "Zkuste zadat prosím nejbližší velké město v oblasti či jeho anglický název."
            )
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
            self.recurrence_set = "Automatické posílání denních menu každý den bylo úspěšně nastaveno/vypnuto."
            self.recurrence_bad = "Byl zadán neplatný čas, automatické posílání bylo nastaveno na 11:00."

        elif lang == "en":
            self.help = (
                    "Hello **{0}**, would you like to know the lunch menu?\n\n"
                    "List of commands:\n\n"
                    "- **{1}  &lt;number&gt;** - to add a favourite restaurant to the personal list\n" +
                    "- **{2} &lt;number&gt;** - to delete a favourite restaurant from the personal list\n"
                    "- **{3}** - to show this help\n"
                    "- **{4} &lt;area&gt;** - to set the city for searching, default is Prague\n"
                    "- **{5} &lt;language&gt;** - to set the language\n"
                    "- **{6}** - to list your favourite restaurants\n"
                    "- **{7} [number]** - to get the lunch menu of a given restaurant\n"
                    "- **{8} [time]** - to set or unset sending the daily menus every day at given time\n"
                    "- **{9} &lt;name&gt;** - to search for a restaurants\n"
                    "- **{10} &lt;number&gt; [time]** - to vote for a restaurant of a day at the given time\n\n"
                    "Glossary:\n"
                    "- **&lt;argument&gt;** - mandatory argument\n"
                    "- **[argument]** - optional argument\n\n"
                    "Examples:\n"
                    "- **{9} Moe's Tavern** - will display list of restaurants Moe's Tavern and their addresses\n"
                    "- **{1} 2** - will add second restaurant from the previous search in the list\n"
                    "- **{7} 1** - will show the lunch menu for the restaurant first in your list\n"
                    "- **{7}** - will print all the daily menus of your favourite restaurants\n\n"
                    "Supported languages:\n"
                    "- **cz** - Czech\n"
                    "- **hr** - Croatian\n"
                    "- **en** - English\n"
                    "- **pl** - Polish\n"
                    "- **ru** - Russian\n"
                    "- **sk** - Slovak\n"
                    "- **tr** - Turkish\n"
            )
            self.welcome_direct = (
                "Hello **{0}**, I am the lunch menu bot.\n\n"
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
            self.city_set = "Area for searching the restaurants successfully set for city of {0}."
            self.city_unknown = (
                "I am sorry, but specified city could not be found. Please try the bigger city in your area."
            )
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
            self.recurrence_set = "Automatic sending of daily menus has been successfully set/unset."
            self.recurrence_bad = "Incorrect time specified, setting automatic sending of menus at 11:00."

        elif lang == "hr":
            self.help = (
                    "Bok **{0}**, želiš li znati dnevni meni?\n\n"
                    "Lista naredbi:\n\n"
                    "- **{1}  &lt;broj&gt;** - za dodavanje omiljenog restorana u personaliziranu listu\n" +
                    "- **{2} &lt;broj&gt;** - za brisanje restorana iz personalizirane liste\n"
                    "- **{3}** - za prikaz pomoći\n"
                    "- **{4} &lt;oblast&gt;** - za postavljanje grada za pretragu, zadano je Prag\n"
                    "- **{5} &lt;jezik&gt;** - za postavljanje jezika\n"
                    "- **{6}** - za ispis tvojih omiljenih restorana\n"
                    "- **{7} [broj]** - za prikaz dnevnog menija\n"
                    "- **{8} [sat]** - postaviti ili deaktivirati dnevne izbornike svaki dan u određeno vrijeme\n"
                    "- **{9} &lt;ime&gt;** - za pretragu restorana\n"
                    "- **{10} &lt;broj&gt; [sat]** - za glasanje za restoran dana za zadano vrijeme\n\n"
                    "Glosar:\n"
                    "- **&lt;argument&gt;** - obavezni argument\n"
                    "- **[argument]** - neobavezni argument\n\n"
                    "Primjeri:\n"
                    "- **{9} Mrzla Piva** - će ispisati sve restorane s imenom Mrzla Piva i njihove adrese\n"
                    "- **{1} 2** - će dodati restoran pod rednim brojem 2 iz prethodne pretrage\n"
                    "- **{7} 1** - će prikazati dnevni meni za prvi restoran u tvojoj listi\n"
                    "- **{7}** - će ispisati sve dnevne menije tvojih omiljenih restorana\n\n"
                    "Podržani jezici:\n"
                    "- **cz** - Češki\n"
                    "- **hr** - Hrvatski\n"
                    "- **en** - Engleski\n"
                    "- **pl** - Polirati\n"
                    "- **ru** - Ruski\n"
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
            self.city_set = "Kao područje za pretragu restorana postavljen je grad {0}."
            self.city_unknown = (
                "Oprosti, ali upisani grad nije pronađen. Molim te unesi veći grad u tvojem području."
            )
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
            self.recurrence_set = "Automatsko dnevno biranje dnevnih izbornika uspješno je postavljeno/deaktivirano."
            self.recurrence_bad = "Postavljeno je vrijeme nevažeće, automatsko slanje postavljeno je na 11:00."

        elif lang == "pl":
            self.help = (
                    "Witaj **{0}**, czy chciałbyś poznać menu lunchowe?\n\n"
                    "Lista poleceń:\n\n"
                    "- **{1}  &lt;numer&gt;** - dodanie ulubionej restauracji do osobistej listy\n" +
                    "- **{2} &lt;numer&gt;** - usuwanie ulubionej restauracji z osobistej listy\n"
                    "- **{3}** - wyświetlenie tej pomocy\n"
                    "- **{4} &lt;obszar&gt;** - aby ustawić miasto do przeszukania, domyślna jest Praga\n"
                    "- **{5} &lt;język&gt;** - zmiana języka\n"
                    "- **{6}** - wyświetlenie listy Twoich ulubionych restauracji\n"
                    "- **{7} [numer]** - wyświetlenie menu lunchowego\n"
                    "- **{8} [godzina]** - codziennie ustawiaj lub dezaktywuj codzienne menu o określonej godzinie\n"
                    "- **{9} &lt;imię&gt;** - wyszukanie restauracji\n"
                    "- **{10} &lt;numer&gt; [godzina]** - aby zagłosować na restaurację na dziś o podanej godzinie\n\n"
                    "Słownik:\n"
                    "- **&lt;argument&gt;** - wymagany argument\n"
                    "- **[argument]** - fakultatywny argument\n\n"
                    "Przykłady:\n"
                    "- **{9} Moe's Tavern** - wyświetlenie listy restauracji Moe's Tavern i ich adresów\n"
                    "- **{1} 2** - dodanie drugiej restauracji z wyników wyszukiwania do listy ulubionych restauracji\n"
                    "- **{7} 1** - wyświetlenie menu lunchowego pierwszej restauracji z listy ulubionych restauracji\n"
                    "- **{7}** - wyświetlenie menu lunchowych wszystkich restauracji z listy\n\n"
                    "Obsługiwane języki:\n"
                    "- **cz** - czeski\n"
                    "- **hr** - chorwacki\n"
                    "- **en** - angielski\n"
                    "- **pl** - polski\n"
                    "- **ru** - rosyjski\n"
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
            self.city_set = "Obszar wyszukiwania restauracji pomyślnie ustawiono na miasto {0}."
            self.city_unknown = (
                "Wybacz, lecz podane miasto nie mogło zostać znalezione. Wybierz większe miasto w swojej okolicy."
            )
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
            self.recurrence_set = (
                "Automatyczne codzienne wybieranie codziennych menu zostało pomyślnie ustawione/dezaktywowane."
            )
            self.recurrence_bad = "Ustalono nieprawidłowy czas, automatyczne wysyłanie zostało ustawione na 11:00."

        elif lang == "ru":
            self.help = (
                "Здравствуйте **{0}**, хотели бы Вы знать, что у нас сегодня в меню?\n\n"
                "Список команд:\n\n"
                "- **{1} &lt;цифра&gt;** - чтобы  добавить ресторан в Список избранных ресторанов\n" +
                "- **{2} &lt;цифра&gt;** - чтобы удалить избранный ресторан из Моего Списка\n"
                "- **{3}** - чтобы показать подсказки\n"
                "- **{4} &lt;область&gt;** - для определения города для поиска, по умолчанию Прага\n"
                "- **{5} &lt;язык&gt;** - чтобы настроить язык\n"
                "- **{6}** - чтобы показать список избранных ресторанов\n"
                "- **{7} [имя}** - получить меню обеданного ресторана\n"
                "- **{8} [время]** - устанавливать или отменять ежедневную отправку ежедневных меню в указанное время\n"
                "- **{9} &lt;цифра&gt;** - чтобы получить меню\n"
                "- **{10} &lt;имя&gt; [время]** - чтобы найти ресторан\n\n"
                "Примечания:\n"
                "- **&lt;аргумент&gt;** - обязательный аргумент\n\n"
                "Примеры:\n"
                "- **{9} Кафе Пушкинъ** - покажет список ресторанов Moe's Tavern и их местоположение\n"
                "- **{1} 2** - добавит второй ресторан из предыдущего поиска\n"
                "- **{7} 1** - покажет меню ресторана, который находится первым в вашем списке\n"
                "- **{7}** - распечатает меню ваших избранных ресторанов \n\n"
                "Поддерживаемые языки:\n"
                "- **cs** - Чешский\n"
                "- **hr** - Хорватский\n"
                "- **en** - Английский\n" 
                "- **pl** - Польский\n"
                "- **ru** - Русский\n"
                "- **sk** - Словацкий\n"
                "- **tr** - Турецкий\n"
            )
            self.unknown = "Извините, я не понимаю. Введите **{0}** ,пожалуйста,  чтобы получить список команд."
            self.not_found = "Извините, но невозможно найти ресторан на основе Вашего ввода."
            self.bad_search = (
                "Извините, но для начала Вы должны ввести номер с предыдущего поиска.\n\n"
                "Попробуйте ввести **{0} &lt;имя&gt;**  чтобы получить список ресторанов"
                "названию а далее **{1} &lt;цифра&gt;** чтобы добавить ресторан в список избранных ресторанов."
            )
            self.add_success = (
                "Ресторан был успешно добавлен в список избранных. Введите **{0}** чтобы отобразить Список "
                "избранных ресторанов Ваших избранных ресторанов."

            )
            self.list_empty = (
                "Ни один избранный ресторан не был найден, добавьте, пожалуйста, "
                "хотя бы один ресторан для использования этой команды."
            )
            self.bad_param = (
                "Извините, но я не могу найти Вами выбранный ресторан. Был введен неправильный номер. "
                "или не был найден соответствующий ресторан списку избранных ресторанов."
            )
            self.del_success = "Ресторан был успешно удален из списка избранных ресторанов."
            self.city_set = "Area for searching the restaurants successfully set for city of {0}."
            self.city_unknown = (
                "I am sorry, but specified city could not be found. Please try the bigger city in your area."
            )
            self.lang_set = (
                "Язык был успешно настроен. Введите **{0}** чтобы отобразить новый список команд на Вашем языке."
            )
            self.lang_unsupported = (
                "Невозможно распознать язык. Возможно этот язык не поддерживается. "
                "Введите **{0}** чтобы отобразить список поддерживаемых языков."
            )
            self.no_menu = "Извините, но Вами заданный ресторан сегодня не предоставил дневное меню."
            self.no_time = (
                "Не было определенно правильное обеденное время, поэтому предполагаю"
                "Ваш сегодняшний обед на ближайший час."
            )
            self.vote_success = (
                "Ваш голос был успешно зарегистрирован, список с коллегам, которые проявили одинаковый интерес, "
                "Вам будет заслан 15 минут до запланированного обеда."
            )
            self.vote_late = "Извините, но сегодняшнее голосование уже закончилось. Попробуйте завтра, пожалуйста."
            self.no_votes = "Извините, но сегодня никто не хочет идти в этот ресторан."
            self.recurrence_set = "Автоматический ежедневный набор ежедневных меню был успешно установлен/деактивирован."
            self.recurrence_bad = (
                "Недействительное время было установлено, автоматическая отправка была установлена на 11:00."
            )

        elif lang == "sk":
            self.help = (
                    "Dobrý deň **{0}**, chcete vediet, čo majú dnes dobré na obed?\n\n"
                    "Zoznam príkazov:\n\n"
                    "- **{1}  &lt;číslo&gt;** - pridá zariadenie na Váš zoznam obľúbených reštaurácií\n" +
                    "- **{2} &lt;číslo&gt;** - odoberie zariadenie z Vášho zoznamu obľúbených reštaurácií\n"
                    "- **{3}** - zobrazí túto nápovedu\n"
                    "- **{4} &lt;oblasť&gt;** - nastaví mesto pre hladanie, predvolená je Praha\n"
                    "- **{5} &lt;jazyk&gt;** - nastaví jazyk\n"
                    "- **{6}** - zobrazí zoznam Vaších obľúbených reštaurácií\n"
                    "- **{7} [číslo]** - zobrazí denné menu zvolenej reštaurácie\n"
                    "- **{8} [čas]** - nastaví alebo vypne posielanie denného menu každý deň v určitom čase\n"
                    "- **{9} &lt;názov&gt;** - vyhľadá zoznam reštaurácií na základe uvedeného názvu\n"
                    "- **{10} &lt;číslo&gt; [čas]** - hlasovanie pre reštauráciu dňa pre zvolený čas\n\n"                    
                    "Vysvetlivky:\n"
                    "- **&lt;argument&gt;** - povinný argument\n"
                    "- **[argument]** - voliteľný argument\n"
                    "Príklady:\n"
                    "- **{9} U Očka** - zobrazí zoznam reštaurácií s názvom U Očka a ich adresy\n"
                    "- **{1} 2** - pridá druhú reštauráciu z predchádzajúceho hľadania na Váš zoznam\n"
                    "- **{7} 1** - zobrazí denné menu reštaurácie na druhej pozícií vo Vašom zozname\n"
                    "- **{7}** - zobrazí všetky denné menu reštaurácií z Vášho zoznamu\n\n"
                    "Podporované jazyky:\n"
                    "- **cz** - čeština\n"
                    "- **hr** - chorvátčina\n"
                    "- **en** - angličtina\n"
                    "- **pl** - polština\n"
                    "- **ru** - ruština\n"
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
            self.city_set = "Oblast pre hladanie reštauracií bola úspešne nastavená na mesto {0}."
            self.city_unknown = (
                "Je mi to ľúto, ale nemôžem nájsť požadované mesto. Skúste zadat najbližšie veľké mesto v oblasti."
            )
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
            self.recurrence_set = "Automatické posielanie denných menu každý deň bolo úspešne nastavené/vypnuté."
            self.recurrence_bad = "Bol zadaný neplatný čas, automatické posielanie bolo nastavené na 11:00."

        elif lang == "tr":
            self.help = (
                    "Merhaba **{0}**, oğlen menüsünü öğrenmek ister misiniz?\n\n"
                    "Komut listesi:\n\n"
                    "- **{1}  &lt;sayı&gt;** - Beğendiğiniz restoranları kişisel listenize ekleyin\n" +
                    "- **{2} &lt;sayı&gt;** - Restoranları kişisel listenizden silin\n"
                    "- **{3}** - Neler yapabileceğimi görün\n"
                    "- **{4} &lt;alan&gt;** - Sehir arayin, guncel sehir Prag\n"
                    "- **{5} &lt;dil&gt;** - Dili değiştirin\n"
                    "- **{6}** - Kişisel restoran listenizi görüntüleyin\n"
                    "- **{7} [sayı]** - Ögle menüsünü oğrenin\n"
                    "- **{8} [zaman]** - Günlük menülere her gün verilen zaman setini ayarlamak veya kaldırmak için\n"
                    "- **{9} &lt;isim&gt;** - Restoranları arayın\n"
                    "- **{10} &lt;sayı&gt; [zaman]** - Bugun restorana ne zaman gideceğini belirten\n\n"
                    "Terimler:\n"
                    "- **&lt;terim&gt;** - Zorunlu terimler\n"
                    "- **[terim]** - Isteğe bağlı terimler\n\n"
                    "Örnekler:\n"
                    "- **{9} Moe's Tavern** - Moe's Tavern isimli restoranları ve adreslerini gösterir\n"
                    "- **{1} 2** - Arama listesindeki ikinci restoranı kişisel listenize ekler\n"
                    "- **{7} 1** - Kişisel listenizdeki ilk restoranın öğle menüsünü gösterir\n"
                    "- **{7}** - Kişisel listenizdeki tüm restoranların öğle menüsünü gösterir\n\n"
                    "Desteklenen diller:\n"
                    "- **cz** - Çekçe\n"
                    "- **hr** - Hırvatça\n"
                    "- **en** - İngilizce\n"
                    "- **pl** - Lehçe\n"
                    "- **ru** - Rusça\n"
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
            self.city_set = "Restoran arama bolgeniz {0} olarak belirlendi."
            self.city_unknown = (
                "Üzgünüm, aradığınız bolge bulunamadi. Lutfen daha genis bir bolgeyi deneyiniz."
            )
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
            self.recurrence_set = "Günlük menülerinin otomatik olarak gönderilmesi başarıyla ayarlandı/çözüldü."
            self.recurrence_bad = "Yanlış saat belirtildi, saat 11:00'de otomatik olarak menü gönderiliyor."

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
            self.city = "oblast"
            self.lang = "jazyk"
            self.list = "seznam"
            self.menu = "menu"
            self.recur = "opakuj"
            self.search = "hledej"
            self.vote = "hlasuj"

        elif lang == "en":
            self.add = "add"
            self.delete = "delete"
            self.help = "help"
            self.city = "city"
            self.lang = "lang"
            self.list = "list"
            self.menu = "menu"
            self.recur = "recur"
            self.search = "search"
            self.vote = "vote"

        elif lang == "hr":
            self.add = "dodaj"
            self.delete = "izbrisi"
            self.help = "pomoc"
            self.city = "grad"
            self.lang = "jezik"
            self.list = "lista"
            self.menu = "meni"
            self.recur = "ponoviti"
            self.search = "pretraga"
            self.vote = "glasaj"

        elif lang == "pl":
            self.add = "dodaj"
            self.delete = "usun"
            self.help = "pomoc"
            self.city = "miasto"
            self.lang = "jezyk"
            self.list = "lista"
            self.menu = "menu"
            self.recur = "powtorz"
            self.search = "wyszukaj"
            self.vote = "glosuj"

        elif lang == "ru":
            self.add = "Добавить"
            self.delete = "Удалить"
            self.help = "помощь"
            self.city = "город"
            self.lang = "язык"
            self.list = "список"
            self.menu = "меню"
            self.recur = "повторяться"
            self.search = "поиск"
            self.vote = "голосуй"

        elif lang == "sk":
            self.add = "pridaj"
            self.delete = "zmaz"
            self.help = "pomoc"
            self.city = "mesto"
            self.lang = "jazyk"
            self.list = "zoznam"
            self.menu = "menu"
            self.recur = "opakuj"
            self.search = "hladaj"
            self.vote = "hlasuj"

        elif lang == "tr":
            self.add = "ekle"
            self.delete = "sil"
            self.help = "yardim"
            self.city = "kent"
            self.lang = "dil"
            self.list = "liste"
            self.menu = "menu"
            self.recur = "tekrar"
            self.search = "ara"
            self.vote = "oyla"

        else:
            raise LangError("ERROR: Unsupported language - {0}.".format(lang))


class LangError(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return repr(self.msg)
