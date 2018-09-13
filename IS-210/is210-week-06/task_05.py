#!/usr/bin/env python
# -*- coding: utf-8 -*0
"""Touching upon the mutability differences between strings and their cousin,
the tuple."""


MYLIST = [(1, 2, 3), 'hello']


def flip_keys(to_flip):
    """This function will take a list that contains a nested list or string
    and reverse their order.

    Args:
        to_flip (list): Parameter 1 needs to be a list. The list is assumed to
            have nested, immutable sequences inside it.

    Returns:
        list: The list returned will be the original list in reverse order.

    Examples:
        >>> flip_keys([(1, 2, 3), 'hello'])
        [(3, 2, 1), 'olleh']

        >>> flip_keys(['hello', 'world', (4, 5, 6)])
        ['olleh', 'dlrow', (6, 5, 4)]

        >>> flip_keys([[12, 13, 14]])
        [[14, 13, 12]]
    """
    newlist = []
    counter = 0
    for value in to_flip:
        newlist.append(value[::-1])
        counter += 1
        to_flip[:counter] = newlist[:counter]
    return to_flip
