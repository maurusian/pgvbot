import pywikibot, sys
from lib.pgvbotLib import *
from copy import deepcopy
import urllib


LIST = [PGOAT,KCLAV,VCLSK,GBART,GMAST,GDEVI,GFAKE,FMOOR,HFROZ,ZWHAT,PGOAT,VSIL1,VSIL2,VWAWA]

site = pywikibot.Site()

pool = site.allpages()


pool_size = len(list(deepcopy(pool)))
print('Pool size: '+str(pool_size))

i = 1
for page in pool:
    print('*********'+str(i)+'/'+str(pool_size))
    try:
        if validate_page(page):
            for CHAR in LIST:
                if CHAR in page.text:
                    print(CHAR+' number '+str(LIST.index(CHAR))+' found in page '+page.title())
                    message = CHAR_FOUND_ON_PAGE_MESSAGE_TEMPLATE.format(CHAR,page.title())
                    log_write(site,message)
            
    except:
        print('Problem searching for char '+CHAR+' found in page '+page.title())
        message = ERROR_MESSAGE_TEMPLATE.format(page.title())
        log_write(site,message)
    i+=1
