# psso-scraper
## Table of Contents
1. [General Info](#general-info)
2. [Packeges](#packeges)
3. [How to use](#how-to-use)

## General Info
This project is a private project. The psso scraper can atomatically log in to a psso account, read the grades
and check if new notes have been added. If this is the case, then the program sends via a telegramm bot (API)
a message with subject and grade to a telegramm account.

## Packeges
- selenium <a href='https://www.selenium.dev/documentation/'>Documentation</a>
- time <a href='https://docs.python.org/3/library/time.html'>Documentation </a>
- pandas <a href='https://pandas.pydata.org/docs/'>Documentation </a>
- xml <a href='https://docs.python.org/3/library/xml.etree.elementtree.html'>Documentation </a>
- math <a href='https://docs.python.org/3/library/math.html'>Documentation </a>

## How to use
To use this program you have to be a registered student of the TH-Köln and have access data to log in to psso. Furthermore, a <a href='https://core.telegram.org/bots/api'>Telegram Bot</a> must be created. In the file "payload" the username and password for the psso account must be stored. In addition, the API key and the chat ID must be stored as well. If everything is given, then only the main.py must be executed. At the first execution two csv files are created. From the second execution on, changes in the note list can be detected.

