#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""A simple for-loop to loop over a simple data construct."""


from decimal import Decimal


def lexicographics(to_analyze):
    """This function will exame the lines of a file or inputted string then
    returns the amount of words in the longest line, the amount of words in the
    shortest line, then calculates the average of words per line in decimal
    format.

    Args:
        to_analyze (str, var): You can input your argument with a string or a
            variable that has a file's data stored.

    Returns:
        tuple: The function will return a tuple containing the amount of words
            in the longest line, the amount of words in the shortest line, then
            calculates the average of words per line in decimal format.

    Examples:
        >>> lexicographics('''Don't stop believing,
        Hold on to that feeling.''')
        (5, 3, Decimal('4'))

        >>> import data
        >>> lexicographics(data.SHAKESPEARE)
        (12, 5, Decimal('8.14'))
    """
    to_analyze = to_analyze.split('\n')
    capdata = []
    longest_line = 0
    shortest_line = 0
    for readwords in to_analyze:
        splitwords = readwords.split()
        capdata.append(len(splitwords))
        longest_line = max(capdata)
        shortest_line = min(capdata)
        calcavg = Decimal(sum(capdata)) / Decimal(len(capdata))
    return longest_line, shortest_line, calcavg
