GLEXI = 'ڭ' #G character found on https://www.lexilogos.com/clavier/araby.htm
GCLAV = 'ݣ' #G character found on many Moroccan keyboards
GFARS = 'گ' #Farsi G
GSTRA = 'ڴ' #Strange G character combining GFARS and GCLAV, who the hell made this shit?
VLEXI = 'ڤ' #V character found on https://www.lexilogos.com/clavier/araby.htm
PLEXI = 'پ' #P character found on https://www.lexilogos.com/clavier/araby.htm

#ALL_PAGES_OPTION = 'a'
LAST_PAGES_OPTION = 'l' #run for last changed pages
G_OPTION = 'g' #change for G characters
P_OPTION = 'p' #change for P characters
V_OPTION = 'v' #change for V characters
REPLACE_FUNC_OPTION = 'r' #run subprogram for in-text replacement
MOVE_FUNC_OPTION = 'm' #run subprogram to move page
ENTRIES_FUNC_OPTION = 'e' #run subprogram to add new entries

G_TEXT_REPLACE_MESSAGE_TEMPLATE = u'پڭڤبوت بدّل {} ڭ ؤ {} گ ؤ {} ڴ ل ݣ' #comment template for text replacement, to be abstracted for any number or type of replacement characters
PAGE_TRANSFER_MESSAGE_TEMPLATE = u"پݣڤبوت حول {} ل [[{}]]" #comment template for page transfer
FIX_REDIRECT_MESSAGE_TEMPLATE = u"پڭڤبوت قاد تّحويل ديال لپاج" #comment for page entry adjustment
ADD_NEW_ENTRY_MESSAGE_TEMPLATE = u'پڭڤبوت زاد دخلة جديدة ل لپاج {}'
ERROR_MESSAGE_TEMPLATE = u'لپاج [[{}]] عطات هاد ليرور\n' #log message for circular redirect error


MOVE_TEXT = u'#تحويل' #code start in transfer page
FILE_CODE_START_TEXT = 'ملف:' #code start in file code
AUDIO_ARTICLE_TAG_TEXT = 'مقال_مهضور' #tag for audio article

BOT_USERNAME = 'PGVBot' #Bot name
BOT_USER_PAGE_TITLE = u'مستخدم:PGVBot' #title of bot user page
LOG_LINE_MESSAGE = u'پڭڤبوت زاد سطر ف لّوڭ' #comment for log entry


REDIRECT_PAGE_CAT_CODE = '[[تصنيف:تحويلات مقالات]]' #category code for transfer page

IGNORE_LIST = ['الصفحة اللّولا'] #list of pages to be completely ignored by the bot, for all tasks
PAGE_TYPE_IGNORE_LIST = ['قالب','تصنيف','ويكيپيديا','إدارة','مستخدم','نقاش المستخدم','باب','نقاش ويكيپيديا','نقاش','نقاش التصنيف'] #list of page types to be completely ignored by the bot, for all tasks
INTEXT_LINE_IGNORE_LIST = ['[[قالب:','{{معلومات مانڭا}}','{{قالب:','[[تصنيف:','{{مقال_مهضور'] #list of sequences for which a line should be ignored for intext replacement, if found
CATEGORY_IGNORE_LIST = ['تصنيف:ليستة د تجاهل ديال پكڤبوت'] #list of categories of pages that will be ignored for intext replacement
