from logging import exception
import localization as lang
import keyboards


# Class with all localization variables
class Locales():

	def __init__(self) -> None:
		menu = {}
		navigation = {}
		basics = {}

	menu = {}
	navigation = {}
	basics = {}
	functions = {}
	pointers = {}
	object_oriented_lang = {}
	exceptions = {}
	containers = {}
	streams = {}
	patterns = {}


# Instance of localization class
locale = Locales()

def set_lang(locale, selected_language):
	locale.menu = lang.RU_MENU if selected_language == "ru" else lang.EN_MENU
	locale.navigation = lang.RU_NAV if selected_language == "ru" else lang.EN_NAV
	locale.basics = lang.RU_BASICS if selected_language == "ru" else lang.EN_BASICS
	locale.functions = lang.RU_FUNCTIONS if selected_language == "ru" else lang.EN_FUNCTIONS
	locale.pointers = lang.RU_POINTERS if selected_language == "ru" else lang.EN_POINTERS
	locale.object_oriented_lang = lang.RU_OOP if selected_language == "ru" else lang.EN_OOP
	locale.exceptions = lang.RU_EXCEPTIONS if selected_language == "ru" else lang.EN_EXCEPTIONS
	locale.containers = lang.RU_CONTAINERS if selected_language == "ru" else lang.EN_CONTAINERS
	locale.streams = lang.RU_STREAMS if selected_language == "ru" else lang.EN_STREAMS
	locale.patterns = lang.RU_PATTERNS if selected_language == "ru" else lang.EN_PATTERNS

# Combines all strings from json into one
def parse_article(article):
	text = ""
	for line in article:
		text += line + "\n"
	return text

# Lists all attributes of a class
def get_attrs(locale=locale):
	members = [attr for attr in dir(locale) if not callable(getattr(locale, attr)) and not attr.startswith("__")]
	return members

# Gets dict data from "xxx.yyy" string
def parse_path(path):
	path = path.split('.')
	for member in get_attrs():
		if path[0] == member:
			dct = getattr(locale, member)
	path.pop(0)
	for p in path:
		dct = dct[p]
	return dct

# Sends default message
async def edit_message(bot, text, callback_query, keyboard):
	if keyboard == locale.menu:
		kb = keyboards.menu(locale.menu)
	else:
		kb = keyboards.generate_keyboard(keyboard)
	
	await bot.edit_message_text(
		text=text, 
		parse_mode="HTML", 
		message_id=callback_query.message.message_id, 
		chat_id=callback_query.from_user.id, 
		reply_markup=kb
	)

# Sends message with navigation buttons
async def edit_message_nav(bot, text, callback_query, article, current_page):
	kb = keyboards.navigation(locale.navigation, article, current_page)
	await bot.edit_message_text(
		text=text, 
		parse_mode="HTML", 
		message_id=callback_query.message.message_id, 
		chat_id=callback_query.from_user.id, 
		reply_markup=kb
	)