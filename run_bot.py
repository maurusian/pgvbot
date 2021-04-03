from lib.pgvbotLib import *
import pywikibot
from sys import argv

def validate_args(args):
    for arg in args:
        if len(arg) == 0 or arg[0] != '-':
            return False
    return True

def validate_page(page):
    if len(page.title().split(':')) == 1 and page.title() not in IGNORE_LIST: #for now only content pages
        return True
    return False

def pool_run(site,pool,target,to_replace,option_string):
    for page in pool:
            
        if validate_page(page):
            if REPLACE_FUNC_OPTION in option_string:
                #call sub program to replace in text
                print(REPLACE_FUNC_OPTION)
                    
                r_page, counters = get_updated_page(page,TARGET,TO_REPLACE)
                    
                if r_page is not None:
                    save_page(r_page,TEXT_REPLACE_MESSAGE_TEMPLATE.format(counters[0],counters[1]))
                else:
                    print("no change")
                    
            if MOVE_FUNC_OPTION in option_string:
                    
                #call sub program to move pages
                page = move_page(page,TARGET,TO_REPLACE)
                
            if ENTRIES_FUNC_OPTION in option_string:
                #call sub program to add new entries to each page
                create_entries(site,page,TARGET,TO_REPLACE)
                fix_redirects(site,page)



if __name__ == '__main__':
    if len(argv)>3:
        local_args = argv[3:]
    else:
        local_args = None

    if local_args is not None and validate_args(local_args):

        option_string = ''.join(local_args)

        dash_count = option_string.count('-')

        option_string = option_string.replace('-','',dash_count)

        print(option_string)
        site = pywikibot.Site()
        if LAST_PAGES_OPTION in option_string:
            
            #load last changed pages (30 days)
            last_changes = site.recentchanges(reverse=True,minor=False,bot=False,redirect=False,excludeuser=BOT_USERNAME)
            pool = [pywikibot.Page(site, item['title']) for item in last_changes if item['type'] == 'edit' and item['user'] != 'PGVBot']
            
        else:
            #load all pages
            pool = site.allpages()
        print(len(list(pool)))
        print(list(pool)[0])
        #a test will be added here for -pgv options

        #if P_OPTION in option_string:
        TARGET = GCLAV
        TO_REPLACE = [GLEXI,GFARS]
        
        for page in pool:
            
            if len(page.title().split(':')) == 1: #for now only content pages
                if REPLACE_FUNC_OPTION in option_string:
                    #call sub program to replace in text
                    print(REPLACE_FUNC_OPTION)
                    
                    r_page, counters = get_updated_page(page,TARGET,TO_REPLACE)
                    
                    if r_page is not None:
                        save_page(r_page,TEXT_REPLACE_MESSAGE_TEMPLATE.format(counters[0],counters[1]))
                    else:
                        print("no change")
                    
                if MOVE_FUNC_OPTION in option_string:
                    
                    #call sub program to move pages
                    page = move_page(page,TARGET,TO_REPLACE)
                
                if ENTRIES_FUNC_OPTION in option_string:
                    #call sub program to add new entries to each page
                    create_entries(site,page,TARGET,TO_REPLACE)
                    fix_redirects(site,page)
            
        #""" 
        
