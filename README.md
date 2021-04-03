# pgvbot

Language: Python3.9
Purpose: Wikipedia Bot

This bot was created to fulfill a specific need in the Moroccan Darija Wikipedia (ary.wikipedia.org). Its functionalities however could be generalized to other projects. The details are explained below. Given that a G sound exists in Moroccan Darija, but not in Standard Arabic, a corresponding letter is needed to represent that sound. Unfortunately, since Moroccan Darija has yet to be standardized, there's no consensus on which G character to use, considering that there are several commonly used:

- GLEXI = 'ڭ' - G character found on https://www.lexilogos.com/clavier/araby.htm
- GCLAV = 'ݣ' - G character found on many Moroccan keyboards
- GFARS = 'گ' - Farsi G
- GSTRA = 'ڴ' - Strange G character combining the forms of GFARS and GCLAV, who the hell made this shit?

The bot performs 3 main tasks:

- In-text replacement of G characters with the target G character which has been agreed upon
- Moving pages with an incorrect G character in the title, to a new title that has the target G
- Adding entries to the same page with other varianst of G in the title

As a side functionality, the bot also corrects the issue of serial redirects (redirects leading to redirects), by making sure all redirect pages lead to the main entry.
The bot should also be able to handle the same process for variants of V and P (see **Future development** section)

## How to run:
If you're an admin on a Moroccan Darija Wiki project:

- Install Python 3.8 or above (preferably Python 3.9)
- Install PyWikiBot, from the Command Line:
```
pip install pywikibot
```
- Clone this repo locally
- Request user-config.py and password.txt from the bot creator, and save both files on the same folder as the Repo clone
- To run the bot, double click on run_bot.bat, this would run with all 3 functionalities for the letter G
- If you want to run with other options, check the Options section

## Options:
The bot cannot run without at least three arguments. The first two are consumed by PyWikiBot module, while the rest are for the bot itself. If less than three arguments are provided, the bot will not do anything.
The available bot options are as follows:

- -l: run for all pages in the recent changes list. If this option is not provided, the bot will run for all pages in the Wiki

- -r: in-text replacement
- -m: move page
- -e: add new entries

- -g: run for the letter G
- -p: run for the letter P
- -v: run for the letter V

The options do not have to be provided seperately. They can for example be written as -lrmepgv or -l -rme -pgv, in no particular order. The dash however is necessary before each letter group, otherwise the function validate_args will return False, and the bot will not run.

# Future development:

# Urgent:
- Checking change types when loading most recently changed pages. So far only 'edit' and 'create' are taken into account. But other change types may also be relevant.
- Completing the abstraction layer so the bot can run for any TARGET, CHARS_TO_REPLACE pair, and for any number of characters in CHARS_TO_REPLACE, which would then be possible to quickly adjust from the main program, without changing the underlying functionalities. This would in principle also make the program more usable for other projects with other languages (see **Using code for other projects**).

# Non-urgent:
- Improving the functionality of adding entries, and the sub-functionality of adjusting entries, by taking X-variants of a redirect pages into accounts. This would imply taking into account the possibility of duplicate pages, which would have to be signaled in the log.
- Improving logging, especially calls and formatting.
- More flexible choice of number of last edited pages or time period. The bot could also save the last run-time, and run only for pages changed from that time.

# Using code for other projects
If you want to build a similar bot for another Wiki project, and you want to use the code, feel free to do so. Please acknowledge this project by putting its name and the link to this Repo in your bot description and/or documentation. The bot could potentially also be useful as it is, for Wiki projects of other Arabic dialects.
I would recommend not using the code until the abstraction is complete though.
For any questions regarding the usage of this bot, or if anything is unclear, please add your question on the [Talk Page](https://ary.wikipedia.org/wiki/%D9%86%D9%82%D8%A7%D8%B4_%D8%A7%D9%84%D9%85%D8%B3%D8%AA%D8%AE%D8%AF%D9%85:Ideophagous). Feel free to write in Moroccan Darija, English, French, German or Arabic.
