import pywikibot, sys
from lib.params import *
from datetime import datetime
import urllib


def cleanup(page,title):
    """
    Adjusts code to ensure special tags and code
    are on a separate line each, which guarantees
    correct treatment.
    This function now returns the text as is, due
    to some issues with tables.
    Will be properly developed in the future.
    """
    text = page.text

    return text #.replace('}}\n','}}').replace('}}','}}\n')

def adjust_file_code(text,target,chars_to_replace):
    """
    corrects image description by replacing specific
    characters with the target character.
    The function will be further abstracted by
    using generic target and char_to_replace variables
    """
    text_parts = text.split('|')
    #counters = [0]*len(char_to_replace)
    COUNTERS = []

    for i in range(len(chars_to_replace)):
        COUNTERS.append(text_parts[-1].count(chars_to_replace[i]))
    """
    GLEXI_COUNTER = text_parts[-1].count(GLEXI)
    GFARS_COUNTER = text_parts[-1].count(GFARS)
    """
    
    if sum(COUNTERS) != 0:

        for i in range(len(chars_to_replace)):
            for j in range(COUNTERS[i]):
                text_parts[-1] = text_parts[-1].replace(chars_to_replace[i],target)

        """
        for i in range(GLEXI_COUNTER):
            text_parts[-1] = text_parts[-1].replace(GLEXI,GCLAV)
        for i in range(GFARS_COUNTER):
            text_parts[-1] = text_parts[-1].replace(GFARS,GCLAV)
        """
    
        text = '|'.join(text_parts)

    return text, COUNTERS
    
def validate_line(line):
    """
    """

    for intext_elem in INTEXT_LINE_IGNORE_LIST:
        if intext_elem in line:
            return False
    return True

#returns page with replaced values (if other forms of G exist)
#returns None otherwise

def get_updated_page(page,target,chars_to_replace):
    """
    Replaces each character element in chars_to_replace
    with target character in page.text
    Returns a tuple of the page and a list containing
    the counts for each character replaced.
    """
    #page = pywikibot.Page(site, title)
    text = page.text

    lines = text.split('\n')
    new_text = ''
    TOTAL_COUNTERS = [0]*len(chars_to_replace)
    """
    TOTAL_GLEXI_COUNTER = 0
    TOTAL_GFARS_COUNTER = 0
    """
    for line in lines:
        #print(line)
        if FILE_CODE_START_TEXT in line:
            line, COUNTERS = adjust_file_code(line,target,chars_to_replace)
            for i in range(len(TOTAL_COUNTERS)):
                TOTAL_COUNTERS[i]+=COUNTERS[i]
            """
            TOTAL_GLEXI_COUNTER+=GLEXI_COUNTER
            TOTAL_GFARS_COUNTER+=GFARS_COUNTER
            """
        elif validate_line(line):

            for i in range(len(chars_to_replace)):
                char_counter = line.count(chars_to_replace[i])
                TOTAL_COUNTERS[i]+=char_counter
                #for j in range(char_counter):
                line = line.replace(chars_to_replace[i],target)

            """
            GLEXI_COUNTER = line.count(GLEXI)
            TOTAL_GLEXI_COUNTER+=GLEXI_COUNTER
            for i in range(GLEXI_COUNTER):
                line = line.replace(GLEXI,GCLAV)

            GFARS_COUNTER = line.count(GFARS)
            TOTAL_GFARS_COUNTER+=GFARS_COUNTER
            for i in range(GFARS_COUNTER):
                line = line.replace(GFARS,GCLAV)
            """
        else:
            #do nothing specific for now
            pass

        new_text+=line+'\n'

    if sum(TOTAL_COUNTERS) != 0:
        page.text = new_text
        return page, TOTAL_COUNTERS
    else:
        return None, [0]*len(chars_to_replace)

def move_page(site,page,target,chars_to_replace):
    """
    Adjusts title with target character and moves
    page to a new title, provided the new title
    is different from the old one
    """
    title = page.title()
    
    
    text = page.text

    
    print('in program')
    if MOVE_TEXT not in text and len(title.split(':'))==1:
        print(title)
        new_title = title

        for i in range(len(chars_to_replace)):
            #char_counter = new_title.count(chars_to_replace[i])
                
            #for i in range(char_counter):
            new_title = new_title.replace(chars_to_replace[i],target)

        """
        GLEXI_COUNT = new_title.count(GLEXI)
        for i in range(GLEXI_COUNT):
            new_title = new_title.replace(GLEXI,GCLAV)

        GFARS_COUNT = new_title.count(GFARS)
        for i in range(GFARS_COUNT):
            new_title = new_title.replace(GFARS,GCLAV)
        """
        
        if new_title != title:
            print('Starting move process')
            new_page = pywikibot.Page(site, new_title)
            if len(new_page.text) == 0:
                message = PAGE_TRANSFER_MESSAGE_TEMPLATE.format(title, new_title)
                pywikibot.output(message)
                page.move(new_title, reason=message, movetalk=True, noredirect=False)
                
                #print(new_title+' about to be moved')
            else:
                print('cannot move to page '+new_title+'. Page already exists!')
                
        else:
            print("no change")
    return page

def create_entries(site,page,target,chars_to_replace):
    """
    Adds new entry pages for a given page, if they
    do not already exist, based on variants obtained
    by replacing target character with characters
    in chars_to_replace.
    """
    title = page.title().strip().replace(" ","_")
    
    if target in page.title():
        try:
            main_entry = title

            
            #target_COUNT = title.count(target)

            for i in range(len(chars_to_replace)):
                #replace target character with variant i
                #for j in range(target_COUNT):
                title = title.replace(target,chars_to_replace[i])

                #replace each variant j with variant i, for j != i
                for j in range(len(chars_to_replace)):
                    if chars_to_replace[j] != chars_to_replace[i]:
                        #char_COUNT = title.count(chars_to_replace[j])
                        #for k in range(char_COUNT):
                        title = title.replace(chars_to_replace[j],chars_to_replace[i])

            
                new_page = pywikibot.Page(site, title)
                if len(new_page.text) == 0:
                    print('creating page entry: '+title)
                    new_page.text = MOVE_TEXT+' [['+main_entry+']]\n\n'+REDIRECT_PAGE_CAT_CODE
                    message = ADD_NEW_ENTRY_MESSAGE_TEMPLATE.format(main_entry)
                    new_page.save(message)

                """
                GLEXI_COUNT = title.count(GLEXI)
                for i in range(GLEXI_COUNT):
                    title = title.replace(GLEXI,GFARS)
                
                new_page = pywikibot.Page(site, title)
                if len(new_page.text) == 0:
                    print('creating page: '+title)
                    new_page.text = MOVE_TEXT+' [['+main_entry+']]'
                    message = comment_message.format(main_entry)
                    new_page.save(message)
                """

        except:
            print('Entry creation failed for entry '+title)
            print(sys.exc_info())

def has_g_char(page,target,chars_to_replace):
    chars = chars_to_replace+[target]
    for char in chars:
        if char in page.title():
            return True
    return False

def get_page_variants(site,page,target,chars_to_replace):
    variants = []

    if not has_g_char(page,target,chars_to_replace):
        return variants

    
    for i in range(len(chars_to_replace)):
        #replace target character with variant i
                
        title = page.title().replace(target,chars_to_replace[i])

        #replace each variant j with variant i, for j != i
        for j in range(len(chars_to_replace)):
            if chars_to_replace[j] != chars_to_replace[i]:
                #char_COUNT = title.count(chars_to_replace[j])
                #for k in range(char_COUNT):
                title = title.replace(chars_to_replace[j],chars_to_replace[i])

            
        variants.append(pywikibot.Page(site, title))
    return variants

def get_page_list_variants(site,page_list,target,chars_to_replace):
    total_variants = []
    page_list_titles = [page.title() for page in page_list]

    for page in page_list:
        variants = get_page_variants(site,page,target,chars_to_replace)
        page_list_titles += [variant.title() for variant in total_variants if variant.title() not in page_list_titles]
        for variant in variants:
            if variant.title() not in page_list_titles:
                total_variants.append(variant)

    return total_variants
        


def get_all_redirects(site,page):
    """
    Implements a recursive process to obtain all pages
    in the redirect tree for a given page
    """
    redirects = None
    try:
        redirects = list(page.getReferences(filter_redirects=True))
    except:
        log_message = ERROR_MESSAGE_TEMPLATE.format(page.title())+sys.exc_info()
        try:
            log_write(site,log_message)
            print(sys.exc_info())
        except:
            print("could not write to log")
            print(sys.exc_info())
    
    if redirects is not None and len(redirects)>0:
        #print(len(redirects))
        for redirect in redirects:
            #print(redirect)
            sub_redirects = get_all_redirects(site,redirect)
            if sub_redirects is not None and len(sub_redirects)>0:
                redirects += sub_redirects
        return redirects
    else:
        return

def log_write(site,message):
    """
    Write to the log page, which is the user page
    of the bot
    """
    user_page = pywikibot.Page(site,BOT_USER_PAGE_TITLE)
    user_page.text += '\n\n\n'+str(datetime.now())+'\n\n\n'+message
    save_page(user_page,LOG_LINE_MESSAGE)
    #user_page.save(LOG_LINE_MESSAGE)

def fix_redirects(site,page,target,chars_to_replace):
    """
    Corrects redirect issues, such as serial redirects
    """
    title = page.title()

    #page = pywikibot.Page(site, title)
    if len(title.split(':'))==1 and MOVE_TEXT not in page.text:
        redirects = get_all_redirects(site,page)

        
        if redirects is not None:
            redirects = get_page_list_variants(site,redirects,target,chars_to_replace)
            transfer_text = MOVE_TEXT + ' [['+title+']]\n\n'+REDIRECT_PAGE_CAT_CODE
            for redirect in redirects:
                if redirect.text != transfer_text:
                    redirect.text = transfer_text
                    try:
                        redirect.save(FIX_REDIRECT_MESSAGE_TEMPLATE)
                    except:
                        #log_message = CIRCULAR_REDIRECT_MESSAGE_TEMPLATE.format(redirect.title())
                        log_message = ERROR_MESSAGE_TEMPLATE.format(redirect.title())+sys.exc_info()
                        try:
                            log_write(site,log_message)
                            print(sys.exc_info())
                        except:
                            print("could not write to log")
                            print(sys.exc_info())

def validate_page(page):
    """
    Verifies if a page is valid for treatment
    or not. For now, only content pages are
    valid for treatment
    """

    if page.title() in IGNORE_LIST or MOVE_TEXT in page.text:
        return False


    page_double_dot_parts = page.title().split(':')
    
    if len(page_double_dot_parts) == 1: #for now only content pages
        return True
    elif len(page_double_dot_parts) > 1 and page_double_dot_parts[0] not in PAGE_TYPE_IGNORE_LIST:
        return True
    return False

def validate_page_text(page):
    """
    Verifies if a page is valid for intext treatment
    or not, by checking the presence of filter
    categories.
    """

    for category in CATEGORY_IGNORE_LIST:
        if category in page.text:
            return False

    return True

def save_page(page,comment):
    """
    Saves page to wikipedia with comment
    """
    try:
        page.save(comment)
    except:
        print("Could not save page "+urllib.parse.quote_plus('https://ary.wikipedia.org/wiki/'+page.title().replace(' ','_')))
        site = pywikibot.Site()
        log_message = ERROR_MESSAGE_TEMPLATE.format(page.title())+str(sys.exc_info())
        try:
            log_write(site,log_message)
        except:
            print("could not write to log")
            print(sys.exc_info())
