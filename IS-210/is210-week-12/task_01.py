#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 01 module"""


def simple_lookup(var1, var2):
    """A simple function that will print the index of argument 1 specified in
    argument 2. If the index is out of bounds, the exception handler will hand
    you a warning message.

    Args:
        var1 (mixed): This can be a list, tuple, or string.
        var2 (int): This will be your index number to print.

    Returns:
        index: The return value will be whatever is indexed at the value of var2
            inside var1.

    Examples:
        >>> simple_lookup('spam', 2)
        a

        >>> simple_lookup((4, 5, 6), 1)
        5

        >>> simple_lookup([1,2],4)
        Warning: Your index/key doesn't exist.
        [1, 2]
    """
    try:
        print var1[var2]
    except LookupError:
        print 'Warning: Your index/key doesn\'t exist.'
    return var1
