#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 02 module"""


import datetime


class InvalidAgeError(Exception):
    """Exception error if age is less than zero"""
    pass


def get_age(birthyear):
    """A simple function that will tell you whether or not you are a living
    human being. Hopefully you are above the age zero.

    Args:
        birthyear (int): This needs to be an integer to work.

    Returns:
        int: Will return your age as an integer.

    Examples:
        >>> get_age(1995)
        23

        >>> get_age(1989)
        29
    """
    age = datetime.datetime.now().year - birthyear
    try:
        if age > 0:
            pass
        else:
            raise InvalidAgeError()
    except InvalidAgeError as age_err:
        raise age_err
    return age
