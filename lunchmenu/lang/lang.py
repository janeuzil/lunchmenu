class Answers(object):
    def __init__(self, lang):
        if lang == "en":
            self.help = (
                "Hello <@personEmail:{0}>, would you like to know the lunch menu?\n\n"
                "List of commands:\n\n"
                "- **{1}  &lt;number&gt;** - to add a favourite restaurant to the personal list\n" +
                "- **{2} &lt;number&gt;** - to delete a favourite restaurant from the personal list\n"
                "- **{3}** - to show this help\n"
                "- **{4} &lt;lang&gt;** - to set the language\n"
                "- **{5}** - to list your favourite restaurants\n"
                "- **{6} &lt;number&gt;** - to get the lunch menu\n"
                "- **{7} &lt;name&gt;** - to search for a restaurants\n\n"
                "Glossary:\n"
                "- **&lt;argument&gt;** - mandatory argument\n\n"
                "Examples:\n"
                "- **{6} 1** - will show the lunch menu for the restaurant first in your list\n"
                "- **{1} 2** - will add second restaurant from the previous search in the list\n\n"
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
            self.unknown = "I am sorry, I do not understand. Please type **help** to get list of commands."

        else:
            raise LangError("Unsupported language - {}.".format(lang))


class Commands(object):
    def __init__(self, lang):
        if lang == "en":
            self.add = "add"
            self.delete = "delete"
            self.help = "help"
            self.lang = "lang"
            self.list = "list"
            self.menu = "menu"
            self.search = "search"

        else:
            raise LangError("Unsupported language - {}.".format(lang))


class LangError(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return repr(self.msg)
