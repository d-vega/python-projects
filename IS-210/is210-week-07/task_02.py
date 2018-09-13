#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Practing the use of ``if`` statements."""


def bool_to_str(bval):
    """This function will test if your passed argument is ``True`` or ``False``.

    Args:
        bval (bool, int, list): The value to pass into your argument can be a
        truthy, falsy, or integer.

    Returns:
        str: A string will be returned to tell you if the value is true or
            false.

    Examples:

        >>> bool_to_str(True)
        'Yes'

        >>> bool_to_str(False)
        'No'

        >>> bool_to_str([1, 2, 3])
        'Yes'
    """
    if bool(bval) == True:
        finalval = 'Yes'
    else:
        finalval = 'No'
    return finalval
