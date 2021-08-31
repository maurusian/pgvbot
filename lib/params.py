#G
GLEXI = 'ڭ' #G character found on https://www.lexilogos.com/clavier/araby.htm
GCLAV = 'ݣ' #G character found on many Moroccan keyboards
GFARS = 'گ' #Farsi G
GSTRA = 'ڴ' #Strange G character combining GFARS and GCLAV, who the hell made this shit?
GMAST = 'ڲ' #Another strange-looking G character, kinda reminds me of a mastodon
GBART = 'ڮ' #G character with a beard
GDEVI = 'ػ' #The devil himself wouldn't think of this
GFAKE = 'چ' #This is not even G, it's a tch sound in Farsi, what's wrong with you people?!

#V
VLEXI = 'ڤ' #V character found on https://www.lexilogos.com/clavier/araby.htm
VWAWA = 'ۋ' #WAW, but with a twist
VSIL1 = 'ۆ' #Some silly waw you got there mate
VSIL2 = 'ۉ' #Some silly waw you got there mate 2
VCLSK = 'ڨ' #The great-grandmother of VLEXI

#P
PLEXI = 'پ' #P character found on https://www.lexilogos.com/clavier/araby.htm
PGOAT = 'ٻ' #P with a goatee

#Other
FMOOR = 'ڢ' #The only F you should want to bring back
HFROZ = 'ھ' #H stuck mid-transformation
ZWHAT = 'ژ' #Emphatic Z, cuz we are emphantic ans shit
KCLAV = 'ک' #The cousin of GCLAV, except she's boring and ugly
ZNORM = 'ز' #Good old fashioned Z
KNORM = 'ك' #K, the boring kind, *yawns*
YFARS = 'ی' #Y used in Persian I think
YNORM = 'ي' #Normal Arabic Y letter
SPACE = ' ' #A single space character, nothing special here

#NAMESPACES
ARTICLE_NAMESPACE = 0


#ALL_PAGES_OPTION = 'a'
LAST_PAGES_OPTION = 'l' #run for last changed pages
CUSTOM_PAGES_OPTIONS = 'c' #run for a list of pages in custom_list.py
G_OPTION = 'g' #change for G characters
P_OPTION = 'p' #change for P characters
V_OPTION = 'v' #change for V characters
REPLACE_FUNC_OPTION = 'r' #run subprogram for in-text replacement
MOVE_FUNC_OPTION = 'm' #run subprogram to move page
ENTRIES_FUNC_OPTION = 'e' #run subprogram to add new entries

G_TEXT_REPLACE_MESSAGE_TEMPLATE = u'پڭڤبوت بدّل {} {} ؤ {} {} ل ݣ' #comment template for text replacement, to be abstracted for any number or type of replacement characters
PAGE_TRANSFER_MESSAGE_TEMPLATE = u"پݣڤبوت حول {} ل [[{}]]" #comment template for page transfer
FIX_REDIRECT_MESSAGE_TEMPLATE = u"پڭڤبوت قاد تّحويل ديال لپاج" #comment for page entry adjustment
ADD_NEW_ENTRY_MESSAGE_TEMPLATE = u'پڭڤبوت زاد دخلة جديدة ل لپاج {}'
ERROR_MESSAGE_TEMPLATE = u'لپاج [[{}]] عطات هاد ليرور\n' #log message for circular redirect error
POTENTIAL_DUPLICATE_TEMPLATE = u'لپاج [[{}]] تقدر تكون مضوبلة'

CHAR_FOUND_ON_PAGE_MESSAGE_TEMPLATE = u'لحرف {} تّلقا ف لپاج [[{}]]'



MOVE_TEXT = u'#تحويل' #code start in transfer page
MOVE_TEXT_EN = "#REDIRECT"
DISAMB_TAG = u"{{توضيح}}" #tag for disambiguation page
FILE_CODE_START_TEXT = 'ملف:' #code start in file code
AUDIO_ARTICLE_TAG_TEXT = 'مقال_مهضور' #tag for audio article

BOT_USERNAME = 'PGVBot' #Bot name
BOT_USER_PAGE_TITLE = u'مستخدم:PGVBot' #title of bot user page
LOG_LINE_MESSAGE = u'پڭڤبوت زاد سطر ف لّوڭ' #comment for log entry


REDIRECT_PAGE_CAT_CODE = '[[تصنيف:تحويلات مقالات]]' #category code for transfer page

IGNORE_LIST = ['الصفحة اللّولا'] #list of pages to be completely ignored by the bot, for all tasks
PAGE_TYPE_IGNORE_LIST = ['قالب','تصنيف','ويكيپيديا','إدارة','قيسارية','نقاش قيسارية','مستخدم','نقاش المستخدم','باب','نقاش ويكيپيديا','نقاش','نقاش التصنيف','نقاش القالب'] #list of page types to be completely ignored by the bot, for all tasks
INTEXT_LINE_IGNORE_LIST = ['[[قالب:','{{معلومات مانڭا}}','{{قالب:','[[تصنيف:','{{مقال_مهضور'] #list of sequences for which a line should be ignored for intext replacement, if found
CATEGORY_IGNORE_LIST = ['تصنيف:ليستة د تجاهل ديال پكڤبوت'] #list of categories of pages that will be ignored for intext replacement



####DarijaBot constants#########


##############################################Stub tag treatment##############################################
###Tags
OLD_STUB_TAG = "{{بذرة}}"
NEW_STUB_TAG = "{{زريعة}}"

###Save messages
CORRECT_STUB_TAG_MESSAGE = "إصلاح طّاڭ د زريعة."
ADD_STUB_TAG_MESSAGE = "زيادة د طّاڭ د زريعة."
REMOVE_STUB_TAG_MESSAGE = "تحياد طّاڭ د زريعة."

##############################################Source header treatment##############################################
###Header patterns
ACCEPTED_SECTION_HEADER_PATTERN = "==\s*عيون\s*لكلام\s*=="
FAULTY_SOURCE_SECTION_HEADERS = ["\\=\\=\s*[ل]{0,1}عيون\s*د\s*لكلام\s*\\=\\="
                                ,"\\=\\=\s*[ل]{0,1}عين\s*[د]{0,1}\s*لكلام\s*\\=\\="
                                ,"\\=\\=\s*[ا]{0,1}[ل]{0,1}مصاد[ي]{0,1}ر\s*\\=\\="
                                ,"\\=\\=\s*[ا]{0,1}[ل]{0,1}م[ا]{0,1}راج[ي]{0,1}ع\s*\\=\\="
                                ,"\\=\\=\s*[ا]{0,1}[ل]{0,1}مصدر\s*\\=\\="
                                ,"\\=\\=\s*[ا]{0,1}[ل]{0,1}مرجع\s*\\=\\="
                                ,"\\=\\=\s*[ل]{0,1}عيون\s*\\=\\="
                                ,ACCEPTED_SECTION_HEADER_PATTERN
                                ]
                                #,"==\s*عيون\s*لكلام\s*=="]
SECTION_HEADER = "== عيون لكلام =="

###Save messages
CORRECT_SOURCE_HEADER_MESSAGE = "إصلاح لهادر د عيون لكلام."
ADD_SOURCE_HEADER_MESSAGE = "زيادة د لهادر د عيون لكلام."



##############################################Source tag treatment##############################################
###Tags
OLD_SOURCE_TAG1 = "{{مراجع}}"
OLD_SOURCE_TAG2 = "<\s*references\s*/>"
NEW_SOURCE_TAG = "{{عيون}}"

###Save messages
CORRECT_SOURCE_TAG_MESSAGE = "إصلاح طّاڭ د عيون لكلام."
ADD_SOURCE_TAG_MESSAGE ="زيادة د طّاڭ د عيون لكلام."

##############################################No category tag treatment##############################################
###Tags
NO_CATEGORY_TAG = "{{مقالة ما مصنفاش}}"

###Save messages
ADD_NO_CAT_TAG_MESSAGE = 'طاڭ ديال "مقالة مامصنفاش" تزاد.'
REMOVE_NO_CAT_TAG_MESSAGE = 'طاڭ ديال "مقالة مامصنفاش" تحيّد.'

##############################################No backlinks tag treatment##############################################
###Tags
ORPHANED_PAGE_TAG = "{{مقالة مقطوعة من شجرة}}"

###Save messages
ADD_ORPHAN_TAG_MESSAGE = 'طاڭ ديال "مقطوعة من شجرة" تزاد.'
REMOVE_ORPHAN_TAG_MESSAGE = 'طاڭ ديال "مقطوعة من شجرة" تحيّد.'


##############################################Authority Control tag##############################################
###Tags
OLD_AUTHORITY_CONTROL_TAG = "{{ضبط استنادي}}"
NEW_AUTHORITY_CONTROL_TAG = "{{ضبط مخازني}}"

###Save messages
FIX_AUTHORITY_CONTROL_TAG = "طّاڭ ديال ضبط مخازني تصلح"
ADD_AUTHORITY_CONTROL_TAG = "طّاڭ ديال ضبط مخازني تزاد"


##############################################Deadend tag##############################################
###Tags
CUL_DE_SAC_TAG = "{{مقالة زنقة ماكاتخرجش}}"

###Save messages

##############################################No sources tag##############################################
###Tags
NO_SOURCES_ON_PAGE_TAG = "{{مقالة ناقصينها عيون لكلام}}"

###Save messages


##############################################Empty paragraph tag##############################################
###Tags
EMPTY_PARAGRAPH_TAG = "{{فقرة مازالا خاوية ولا ناقصة}}"

###Save messages

##############################################OTHER STRUCTURES##############################################
###Tags
INFOBOX_TAG_PATTERN = r"{{معلومات.*}}"

MONTHS = [{"en_name":"January","ary_name":u"يناير","day_count":31,"alt_name":""}
         ,{"en_name":"February","ary_name":u"فبراير","day_count":29,"alt_name":u"يبراير"}
         ,{"en_name":"March","ary_name":u"مارس","day_count":31,"alt_name":""}
         ,{"en_name":"April","ary_name":u"أبريل","day_count":30,"alt_name":""}
         ,{"en_name":"May","ary_name":u"ماي","day_count":31,"alt_name":""}
         ,{"en_name":"June","ary_name":u"يونيو","day_count":30,"alt_name":""}
         ,{"en_name":"July","ary_name":u"يوليوز","day_count":31,"alt_name":""}
         ,{"en_name":"August","ary_name":u"غشت","day_count":31,"alt_name":""}
         ,{"en_name":"September","ary_name":u"شتنبر","day_count":30,"alt_name":""}
         ,{"en_name":"October","ary_name":u"أكتوبر","day_count":31,"alt_name":u"كتوبر"}
         ,{"en_name":"November","ary_name":u"نونبر","day_count":30,"alt_name":""}
         ,{"en_name":"December","ary_name":u"دجنبر","day_count":31,"alt_name":""}]
