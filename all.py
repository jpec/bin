#!/usr/bin/python3

import os

XMLHEAD = "<ul>"
XMLBLOC = "<li><a href=\"{0}\">{1}</a></li>"
XMLFOOT = "</ul>"
WWWROOT = "http://www.peclu.net/~"
DIRROOT = "/home/{0}/www/"
USERS = ["peclu", "julien", "pimp", "raspyplayer", "gunsmith"]

def print_sitemap(users):
    print(XMLHEAD)
    for user in users:
        for page in os.listdir(DIRROOT.format(user)):
            if page[-4:] == "html":
               print(XMLBLOC.format(WWWROOT+user+"/"+page, user+"/"+page))
    print(XMLFOOT)

def main():
    print_sitemap(USERS)

main()
