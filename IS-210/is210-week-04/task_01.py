#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This module provides a function that knows what you mean"""


def know_what_i_mean(wink, numwink=2):
    """A simple function that accepts a **str** argument and an **int**
    argument.

    When the function is called, the arguments passed will be returned
    in a sentence.

    Args:
        wink (str): The first parameter that can only contain a str.
        winks (str): Local variable that containts the new str created after
            multiplying **wink**.
        nudges (str): Local variable that also gets multiplied by second
            argument passed.
        retstr (str): Another local str variable that will contain the final
            formatted str that will be returned including **winks** and
            **nudges** in the returned statement.
        numwink (int, optional): The second parameter that needs an int. The
            int passed will be the number that **wink** and **nudges** gets
            multiplied by. Default: 2

    Returns:
        str: Argument 1 multiplied by Argument 2 inside the local variable
            returned.

    Examples:

        >>> know_what_i_mean('wink ')
        'Know what I mean? wink wink, nudge nudge'

        >>> know_what_i_mean('hey ')
        'Know what I mean? hey hey, nudge nudge'

        >>> know_what_i_mean('wink ', 3)
        'Know what I mean? wink wink wink, nudge nudge nudge'
    """
    winks = (wink * numwink).strip()
    nudges = ('nudge ' * numwink).strip()
    retstr = 'Know what I mean? {}, {}'.format(winks, nudges)
    return retstr
