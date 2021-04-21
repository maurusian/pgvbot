from lib.pgvbotLib import *
import pywikibot
from copy import deepcopy
from sys import argv


def validate_args(args):
    """
    Checks if args are valid
    """
    for arg in args:
        if len(arg) == 0 or arg[0] != '-':
            return False
    return True

def pool_run(site,pool,target,to_replace,option_string):
    """
    Runs routine for a pool of pages
    Subprograms are called depending on the
    selected options, provided as arguments (args).

    
    """
    i = 1
    pool_size = len(list(deepcopy(pool)))
    for page in pool:
        print('*********'+str(i)+'/'+str(pool_size))
        
        if validate_page(page):
            
                
            if REPLACE_FUNC_OPTION in option_string and validate_page_text(page):
                #call sub program to replace in text
                print(REPLACE_FUNC_OPTION)
                    
                r_page, counters = get_updated_page(page,target,to_replace)
                    
                if r_page is not None:
                    save_page(r_page,G_TEXT_REPLACE_MESSAGE_TEMPLATE.format(counters[0],counters[1],counters[2]))
                else:
                    print("no change")
                    
            if MOVE_FUNC_OPTION in option_string:
                    
                #call sub program to move pages
                page = move_page(site,page,target,to_replace)
                
            if ENTRIES_FUNC_OPTION in option_string:
                #call sub program to add new entries to each page
                
                create_entries(site,page,target,to_replace)
                fix_redirects(site,page)
        i+=1


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
            
            #load last changed
            last_changes = site.recentchanges(reverse=True,minor=False,bot=False,redirect=False,excludeuser=BOT_USERNAME)
            #create page pool
            #NEXT: check other potential last_change types
            pool = [pywikibot.Page(site, item['title']) for item in last_changes if (item['type'] == 'edit' or item['type'] == 'create') and item['user'] != 'PGVBot']
            
        else:
            #load all pages, default option
            pool = site.allpages()

        pool_size = len(list(deepcopy(pool)))
        print('Pool size: '+str(pool_size))
        
        #a test will be added here for -pgv options

        if G_OPTION in option_string:
            TARGET = GCLAV
            TO_REPLACE = [GLEXI,GFARS,GSTRA]

            #run for all pages in pool
            pool_run(site,pool,TARGET,TO_REPLACE,option_string)
                
        #""" 
        
