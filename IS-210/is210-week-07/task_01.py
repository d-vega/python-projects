#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""A Fibonacci sequence generator using a ``while`` loop"""


def fibonacci(maxint):
    """Performing the Fibonacci sequence. The results will be returned as a
    list.

    Args:
        maxint (int): Pass a max integer you want the ``while`` loop inside the
            function reference as the end point of the loop.

    Returns:
        list: The results of the fibonacci sequence will be returned as a list.

    Examples:

        >>> fibonacci(10)
        [1, 1, 2, 3, 5, 8]

        >>> fibonacci(20)
        [1, 1, 2, 3, 5, 8, 13]
    """
    lastnum, curnum = 0, 1
    mklist = [0]
    while curnum < maxint:
        mklist.append(curnum)
        lastnum, curnum = curnum, lastnum + curnum
    return mklist
