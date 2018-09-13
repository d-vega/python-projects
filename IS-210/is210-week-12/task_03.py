#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 03 module"""


import time


class CustomLogger(object):
    """A logger class checking for file existance and logging errors"""

    def __init__(self, logfilename):
        """Constructor for CustomLogger

        Args:
            logfilename (str): This should be the name of the file to open and
                log to.

        Returns:
            file: Will create a log file if it does not exist.
        """
        self.logfilename = logfilename
        self.msgs = []

    def log(self, msg, timestamp=None):
        """Entries for log errors.

        Args:

            msg (string): This will be the entry description.
            timestamp (str): The time the entry was logged.

        Returns:

            list: Will append the strings to the self.msgs list.

        Examples:

            >>> myinst = CustomLogger('bad.txt')
            >>> myinst.log('hello')
            >>> print myinst.msgs
            >>> [(1524715057.743972, 'hello')]
        """
        if timestamp is None:
            timestamp = time.time()
        self.msgs.append((timestamp, msg))

    def flush(self):
        """This will create the log file if it does not exists. If it does exist
        it will write some entries to it then remove."""
        handled = []
        try:
            fhandler = open(self.logfilename, 'a')
        except IOError as no_file_exists:
            self.log(no_file_exists)
            raise no_file_exists
        else:
            try:
                for index, entry in enumerate(self.msgs):
                    fhandler.write(str(entry) + '\n')
                    handled.append(index)
            finally:
                fhandler.close()
                for index in handled[::-1]:
                    del self.msgs[index]
