#!/usr/bin/python3

import os
import sys

XMLHEAD = "<urlset xmlns=\"http://www.sitemaps.org/schemas/sitemap/0.9\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xsi:schemaLocation=\"http://www.sitemaps.org/schemas/sitemap/0.9 http://www.sitemaps.org/schemas/sitemap/0.9/sitemap.xsd\">"
XMLBLOC = "<url><loc>{0}</loc><lastmod>{1}</lastmod><changefreq>daily</changefreq><priority>0.5</priority></url>"
XMLFOOT = "</urlset>"
WWWROOT = "http://www.peclu.net/~"
DIRROOT = "/home/{0}/www/"
USERS = ["peclu", "pimp", "raspyplayer", "gunsmith", "julien"]


def get_date():
    if len(sys.argv) == 2 and len(sys.argv[1]) == 10:
        return(sys.argv[1])
    else:
        return(None)

def print_sitemap(date, users):
    print(XMLHEAD)
    for user in users:
        for page in os.listdir(DIRROOT.format(user)):
            if page[-4:] == "html":
               print(XMLBLOC.format(WWWROOT+user+"/"+page, date))
    print(XMLFOOT)

def main():
    date = get_date()
    if date:
        print_sitemap(date, USERS)
    else:
        print("Usage: {0} <date>".format(sys.argv[0]))

main()
