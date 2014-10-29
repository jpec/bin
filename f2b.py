#!/usr/bin/env python3

import mailbox
import os
import sys

def open_mbox(box):
    if os.path.isfile("/var/mail/"+box):
        mbox = mailbox.mbox("/var/mail/"+box)
        mbox.lock()
        return(mbox)
    else:
        return(None)

def close_mbox(mbox):
    mbox.flush()
    mbox.unlock()
    mbox.close()
    return(True)

def treat_message(message):
    if message['from'] == 'fail2ban@peclu.net':
        return(message['date'] + " - " + message['subject'])
    else:
        return(None)

def reading_messages(mbox):
    f2b_messages = list()
    for key in mbox.keys():
        unread = treat_message(mbox.get(key))
        if unread:
            f2b_messages.append(unread)
    return(f2b_messages)

def main(args):
    if len(args) == 2:
        mbox = open_mbox(args[1])
        if mbox:
            f2b_messages = reading_messages(mbox)
            close_mbox(mbox)
            print("Nb unread mail(s):", len(f2b_messages))
            for message in f2b_messages:
                print(">", message)
        else:
            print("Oops. Cannot open the mailbox", args[1])
    else:
        print("Usage:", args[0], "mailbox")


main(sys.argv)
# EOF
