import pywikibot, sys
from copy import deepcopy
from lib.params import FILE_CODE_START_TEXT, MOVE_TEXT
from lib.pgvbotLib import validate_line



site = pywikibot.Site()

print(help(site.recentchanges))

pool = site.allpages()

character_set_dict = {}

pool_size = len(list(deepcopy(pool)))
print("Pool size: "+str(pool_size))

i=1
for page in pool:
    print(str(i)+'/'+str(pool_size))
    if MOVE_TEXT not in page.text:
        print("Start treatment for :"+page.title())
        print("Number of characters :"+str(len(page.text)))
        for line in page.text.splitlines():
            if validate_line(line):
                if FILE_CODE_START_TEXT in line:
                    line = line #special treatment
                for char in line:
                    if ord(char)>255:
                        if char in character_set_dict.keys():
                            character_set_dict[char]+=1
                        else:
                            character_set_dict[char]=1

    i+=1

character_set_list = [(k, v) for k, v in character_set_dict.items()]

try:
    character_set_list.sort(key=lambda x:x[1])

except:
    print("Could not sort list")
    print(sys.exc_info())

for elem in character_set_list:
    print(elem[0]+'  '+str(elem[1]))
