import pywikibot, sys
from lib.params import *
from datetime import datetime


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

def adjust_file_code(text,target,char_to_replace):
    """
    corrects image description by replacing specific
    characters with the target character.
    The function will be further abstracted by
    using generic target and char_to_replace variables
    """
    text_parts = text.split('|')
    GLEXI_COUNTER = text_parts[-1].count(GLEXI)
    GFARS_COUNTER = text_parts[-1].count(GFARS)
    
    if GLEXI_COUNTER != 0 or GFARS_COUNTER != 0:

        for i in range(GLEXI_COUNTER):
            text_parts[-1] = text_parts[-1].replace(GLEXI,GCLAV)
        for i in range(GFARS_COUNTER):
            text_parts[-1] = text_parts[-1].replace(GFARS,GCLAV)

    
        text = '|'.join(text_parts)

    return text, GLEXI_COUNTER, GFARS_COUNTER
    


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
    TOTAL_GLEXI_COUNTER = 0
    TOTAL_GFARS_COUNTER = 0
    for line in lines:
        #print(line)
        if 'ملف:' in line:
            line, GLEXI_COUNTER, GFARS_COUNTER = adjust_file_code(line,target,chars_to_replace)
            TOTAL_GLEXI_COUNTER+=GLEXI_COUNTER
            TOTAL_GFARS_COUNTER+=GFARS_COUNTER
            
        elif 'مقال_مهضور' not in line:
            
            GLEXI_COUNTER = line.count(GLEXI)
            TOTAL_GLEXI_COUNTER+=GLEXI_COUNTER
            for i in range(GLEXI_COUNTER):
                line = line.replace(GLEXI,GCLAV)

            GFARS_COUNTER = line.count(GFARS)
            TOTAL_GFARS_COUNTER+=GFARS_COUNTER
            for i in range(GFARS_COUNTER):
                line = line.replace(GFARS,GCLAV)
                
        else:
            #print(line)
            pass

        new_text+=line+'\n'

    #print(new_text)
    if TOTAL_GLEXI_COUNTER != 0 or TOTAL_GFARS_COUNTER != 0:
        page.text = new_text
        return page, [TOTAL_GLEXI_COUNTER, TOTAL_GFARS_COUNTER]
    else:
        return None, [0, 0]

def move_page(page,target,chars_to_replace):
    """
    """
    title = page.title()
    
    
    text = page.text

    
    print('in program')
    if MOVE_TEXT not in text and len(title.split(':'))==1:
        print(title)
        new_title = title

        GLEXI_COUNT = new_title.count(GLEXI)
        for i in range(GLEXI_COUNT):
            new_title = new_title.replace(GLEXI,GCLAV)

        GFARS_COUNT = new_title.count(GFARS)
        for i in range(GFARS_COUNT):
            new_title = new_title.replace(GFARS,GCLAV)

        print('running title test')
        if new_title != title:
            print('starting process')
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
    """
    title = page.title().strip().replace(" ","_")
    
    if GCLAV in page.title():
        try:
            main_entry = title
            GCLAV_COUNT = title.count(GCLAV)
            for i in range(GCLAV_COUNT):
                title = title.replace(GCLAV,GLEXI)
            GFARS_COUNT = title.count(GFARS)
            for i in range(GFARS_COUNT):
                title = title.replace(GFARS,GLEXI)
            new_page = pywikibot.Page(site, title)
            if len(new_page.text) == 0:
                print('creating page: '+title)
                new_page.text = '#تحويل [['+main_entry+']]'
                message = comment_message.format(main_entry)
                new_page.save(message)

            GLEXI_COUNT = title.count(GLEXI)
            for i in range(GLEXI_COUNT):
                title = title.replace(GLEXI,GFARS)
            
            new_page = pywikibot.Page(site, title)
            if len(new_page.text) == 0:
                print('creating page: '+title)
                new_page.text = '#تحويل [['+main_entry+']]'
                message = comment_message.format(main_entry)
                new_page.save(message)

        except:
            print('Entry creation failed for entry '+title)
            print(sys.exc_info())

def get_all_redirects(site,page):
    redirects = None
    try:
        redirects = list(page.getReferences(filter_redirects=True))
    except:
        log_message = CIRCULAR_REDIRECT_MESSAGE_TEMPLATE.format(page.title())
        log_write(site,log_message)
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
    user_page = pywikibot.Page(site,BOT_USER_PAGE_TITLE)
    user_page.text += '\n\n\n'+str(datetime.now())+'\n\n\n'+message
    save_page(user_page,LOG_LINE_MESSAGE)
    #user_page.save(LOG_LINE_MESSAGE)

def fix_redirects(site,page):
    title = page.title()

    #page = pywikibot.Page(site, title)
    if len(title.split(':'))==1 and MOVE_TEXT not in page.text:
        redirects = get_all_redirects(site,page)

        
        if redirects is not None:
            transfer_text = MOVE_TEXT + ' [['+title+']]\n\n[[تصنيف:تحويلات مقالات]]'
            for redirect in redirects:
                if redirect.text != transfer_text:
                    redirect.text = transfer_text
                    try:
                        redirect.save(FIX_REDIRECT_MESSAGE_TEMPLATE)
                    except:
                        #log_message = CIRCULAR_REDIRECT_MESSAGE_TEMPLATE.format(redirect.title())
                        log_write(site,sys.exc_info())
                        print(sys.exc_info())

def save_page(page,comment):
    """
    """
    page.save(comment)
