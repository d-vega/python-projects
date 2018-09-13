#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Iterating through a dictionary object"""


DATA = {
    1: 10,
    2: 20,
    3: 30,
    4: 40,
    5: 50,
    6: 60,
    7: 70,
    8: 80,
    9: 90,
    10: 100
    }


def iter_dict_funky_sum(mydict):
    """A function that will get the product of your dictionary values minus the
    keys then add up the total.

    Args:
        mydict (dict): The argument passed needs to be a dictionary with
            integers for both the keys and values.

    Returns:
        int: Will first calculate the product of your values minus the keys then
            add them to the total.

    Examples:
        >>> iter_dict_funky_sum(DATA)
        495

        >>> iter_dict_funky_sum({10: 52, 11: 59, 12: 90, 13: 432, 14: 25, 15: 18
        9, 16: 230, 17: 231, 18: 223, 19: 456, 20: 9587})
        11409
    """
    total = 0
    for datkeys, datvalues in mydict.iteritems():
        total += datvalues - datkeys
    return total
