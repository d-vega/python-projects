#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Schedule a time for your alarm to go off and the command line will let you
know"""


import random
import time
import webbrowser


SETHOUR = raw_input('What time do you want to wake up? First enter the hour'
                    ' (i.e. 04, 05, 12): ')
SETMINUTE = raw_input('\nGot it, now set the minute of the hour (i.e. 12, 32,'
                      ' 01): ')
DAY_OR_AFT = raw_input('\nOkay, AM or PM? ').upper()
ALARMSET = '{}:{} {}'.format(SETHOUR, SETMINUTE, DAY_OR_AFT)
TIME = time.strftime('%I:%M %p')
GO_OFF = "\nIt\'s time! DING! DING! DING!"
LINKS = []


print '\nYour alarm has been set to go off at {}.\n'.format(ALARMSET)


def separate_links(opened_file):
    """This function will separate the URL links in the 'YT.txt' file. The
    output is then used later to choose a link at random for when the alarm sets
    off.

    Args:
        opened_file (var): This program will always use the YT_FILE variable to
            pass into this argument. If you use it outside the scope of this
            intended use, please save your file into a new variable to pass
            here.

    Returns:
        opened_file.close() (function): This will close the file in the passed
            variable within the argument.
    """
    for lines in opened_file:
        striplines = lines.rstrip('\n')
        LINKS.append(striplines)
    return opened_file.close()


try:
    YT_FILE = open('YT.txt', 'r')
except IOError:
    print 'Sorry, the system cannot find "YT.txt" in your file path.'
    print 'Creating file . . .'
    YT_FILE = open('YT.txt', 'w')
    YT_FILE.write('https://www.youtube.com/watch?v=iNpXCzaWW1s\n')
    YT_FILE.write('https://www.youtube.com/watch?v=gVCNPalH8MA\n')
    YT_FILE.close()
    print 'Success! "YT.txt" has been created.'
    YT_FILE = open('YT.txt', 'r')
    LINKS = []
    separate_links(YT_FILE)
else:
    separate_links(YT_FILE)


def open_alarm_link(link_names):
    """Simple function that will open a random URL from your YT.txt file.

    Args:
        link_names (str, var): This will be the str or var containing the URL's
            from the YT.txt file.

    Returns:
        openurl (function): This will open up a random URL from the YT.txt file
            in your default web browser.
    """
    print GO_OFF
    time.sleep(1)
    openurl = webbrowser.open_new_tab(random.choice(link_names))
    return openurl


if TIME == ALARMSET:
    open_alarm_link(LINKS)
else:
    while TIME != ALARMSET:
        CURTIME = time.strftime('%I:%M %p')
        COUNT_DOWN = time.strftime('%I:%M:%S %p')
        print "The time currently is: {}".format(COUNT_DOWN)
        if CURTIME == ALARMSET:
            open_alarm_link(LINKS)
            break
        else:
            time.sleep(1)
