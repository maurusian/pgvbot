from lib.pgvbotLib import *
import pywikibot
from copy import deepcopy
from sys import argv
from data.custom_pool import page_list
import os

RECENT_LOG_FILE = "recent_log.txt"

def load_pages_in_log():
    if not os.path.exists(RECENT_LOG_FILE):
        return []
    with open(RECENT_LOG_FILE,'r',encoding='utf-8') as f:
        page_name_list = f.read().strip().splitlines()
    
    for i in range(len(page_name_list)):
        page_name_list[i] = page_name_list[i].strip()
    return page_name_list


def validate_args(args):
    """
    Checks if args are valid
    """
    for arg in args:
        if len(arg) == 0 or arg[0] != '-':
            return False
    return True

def pool_run(site, pool, target, list_to_replace1, list_to_replace2, option_string):
    """
    Runs routine for a pool of pages
    Subprograms are called depending on the
    selected options, provided as arguments (args).

    
    """
    i = 1
    pool_size = len(list(deepcopy(pool)))
    pages_in_log = load_pages_in_log()
    with open(RECENT_LOG_FILE,'a',encoding='utf-8') as f:
        for page in pool:
            print('*********'+str(i)+'/'+str(pool_size))
            
            if str(page.title()) not in pages_in_log and validate_page(page):
                
                    
                if REPLACE_FUNC_OPTION in option_string and validate_page_text(page):
                    #call sub program to replace in text
                    print(REPLACE_FUNC_OPTION)
                        
                    r_page, counters = get_updated_page(page,target,list_to_replace1)
                        
                    if r_page is not None:
                        save_page(r_page,G_TEXT_REPLACE_MESSAGE_TEMPLATE.format(counters[0],list_to_replace1[0],counters[1],list_to_replace1[1]))
                    else:
                        print("no change from list 1")

                    r_page, counters = get_updated_page(page,target,list_to_replace2)
                        
                    if r_page is not None:
                        save_page(r_page,G_TEXT_REPLACE_MESSAGE_TEMPLATE.format(counters[0],list_to_replace2[0],counters[1],list_to_replace2[1]))
                    else:
                        print("no change from list 2")
                        
                if MOVE_FUNC_OPTION in option_string:
                        
                    #call sub program to move pages
                    page = move_page(site,page,target,list_to_replace1)
                    page = move_page(site,page,target,list_to_replace2)
                    
                if ENTRIES_FUNC_OPTION in option_string:
                    #call sub program to add new entries to each page

                    create_entries(site,page,target,list_to_replace1)
                    fix_redirects(site,page,target,list_to_replace1)
            
            i+=1
            f.write(page.title()+'\n')


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
            last_changes = site.recentchanges(reverse=True,minor=False,bot=False,redirect=False,top_only=True)
            #create page pool
            #NEXT: check other potential last_change types

            pool = [pywikibot.Page(site, item['title']) for item in last_changes if (item['type'] == 'edit' or item['type'] == 'new') and item['user'] != 'PGVBot']

            
        elif CUSTOM_PAGES_OPTIONS in option_string:
            
            pool = [pywikibot.Page(site, title.strip()) for title in page_list.strip().split()]
            
        else:

            #load all pages on the article namespace, default option
            pool = site.allpages(namespace=ARTICLE_NAMESPACE)


        pool_size = len(list(deepcopy(pool)))
        print('Pool size: '+str(pool_size))
        
        #a test will be added here for -pgv options

        if G_OPTION in option_string:
            TARGET = GCLAV
            LIST_TO_REPLACE1 = [GLEXI,GFARS]
            LIST_TO_REPLACE2 = [GSTRA,GFAKE]

            #run for all pages in pool
            pool_run(site, pool, TARGET, LIST_TO_REPLACE1, LIST_TO_REPLACE2, option_string)
                
        #""" 
        
