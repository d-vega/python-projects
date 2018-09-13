#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Practicing looping lists with a **for** loop"""


def process_data(data):
    """This function will give you the sum and average of a list or tuple and
    returns the values as a tuple.

    Args:
        data (list, tuple): Parameter 1 needs to be a list or a tuple.

    Returns:
        tuple: The tuple returned provides you the sum at index 0 and the
            average at index 1.

    Examples:

        >>> process_data((1, 2, 3))
        (6, 2.0)

        >>> process_data([2, 4, 6])
        (12, 4.0)

        >>> process_data((4, 7, 8))
        (19, 6.0)
    """
    data_sum = 0
    for add_values in data:
        data_sum += add_values
        mklist = [data_sum, float(sum(data)) / float(len(data))]
    return tuple(mklist)
