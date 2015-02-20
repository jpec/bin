#!/usr/bin/python3

import os
import sys

XMLHEAD = "<urlset xmlns=\"http://www.sitemaps.org/schemas/sitemap/0.9\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xsi:schemaLocation=\"http://www.sitemaps.org/schemas/sitemap/0.9 http://www.sitemaps.org/schemas/sitemap/0.9/sitemap.xsd\">"
XMLBLOC = "<url><loc>{0}</loc><lastmod>{1}</lastmod><changefreq>daily</changefreq><priority>0.5</priority></url>"
XMLFOOT = "</urlset>"
WWWROOT = "http://{0}/~{1}/{2}"
DIRROOT = "/home/{0}/www/"


def get_date():
    if len(sys.argv) >= 2 and len(sys.argv[1]) == 10:
        return(sys.argv[1])
    else:
        return(None)

def get_root():
    if len(sys.argv) >= 3:
        return(sys.argv[2])
    else:
        return(None)

def get_users():
    if len(sys.argv) >= 4:
        return(sys.argv[3:])
    else:
        return(None)

def print_sitemap(date, root, users):
    print(XMLHEAD)
    for user in users:
        for page in os.listdir(DIRROOT.format(user)):
            if page[-4:] == "html":
               print(XMLBLOC.format(WWWROOT.format(root,user,page), date))
    print(XMLFOOT)

def main():
    date = get_date()
    root = get_root()
    users = get_users()
    if date and root and users:
        print_sitemap(date, root, users)
    else:
        print("Usage: {0} <date> <www> <user1> <user2> [...]".format(sys.argv[0]))

main()
