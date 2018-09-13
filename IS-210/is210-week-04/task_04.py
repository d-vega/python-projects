#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Practicing functions by passing arguments to function parameters, and
creating docstrings.

"""


def too_many_kittens(kittens, litterboxes, catfood):
    """A function that makes sure there's at least one litterbox for each
    kitten you have as well as check if you have catfood.

    Args:
        kittens (int): Parameter 1 should pass an int for the number of
            kittens.
        litterboxes (int): Parameter 2 should pass an int for the number of
            litterboxes available.
        catfood (bool, int): Parameter 3 will need a boolean passed. This can be
            a value of ``None``, ``True``, ``False``, ``0``, or ``1``.
        take_care_of_kittens (bool): Local variable returned that will check
            for at least one litterbox for each kitten then inverts the third
            argument.

    Returns:
        bool:

    Examples:

        >>> too_many_kittens(12, 12, False)
        True

        >>> too_many_kittens(12, 13, True)
        False

        >>> too_many_kittens(12, 13, 1)
        False
    """
    take_care_of_kittens = not (litterboxes >= kittens and catfood)
    return take_care_of_kittens
