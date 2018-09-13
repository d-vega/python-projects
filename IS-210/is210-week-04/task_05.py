#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Practicing the order of function parameters."""


def defaults(my_required, my_optional=True):
    """A simple function that compares the boolean values of two arguments
    to see if they are equal to each other.

    Args:
        my_required (bool, int): First parameter that can have a boolean value
            or integer of ``0`` or ``1``.
        my_optional (bool, int, optional): Second parameter that is optional. It
            can have a boolean value or integer of ``0`` or ``1``. Default: True

    Returns:
        bool: Returns a boolean value based on whether or not Argument 1 is
            equal to Argument 2.

    Examples:

        >>> defaults(True)
        True

        >>> defaults(True, False)
        False

        >>> defaults(False, False)
        True
    """
    return my_optional is my_required
