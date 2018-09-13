#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Provides an interface to data-bearing functions."""

import json
import os


BALLETS = ['The Nutcracker',
           'Duck Lake',
           'Sleeping Beauty',
           'Onegin',
           'Manon',
           'Le Corsair',
           'Serenade',
           'Agon',
           'Apollo',
           'Scherehazade',
           'Giselle',
           'Amadeus',
           'Robert Schumann\'s "Davids Bundlertanze"',
           'Firebird',
           'Concerto Barocco',
           'Napoli',
           'A Midsummer Night\'s Dream',
           'La Bayadere',
           'Romeo and Juliet',
           'Jewels',
           'The Four Temperaments',
           'La Valse']

DIRECTIONS = ('North', 'South', 'East', 'Spaghetti Western')


def get_raw_data():
    """Loads our data from file and returns it.

    Returns:
        list: A list of serialized data.

    Examples:
        >>> get_raw_data()
        [578, 389, ...]
    """
    fpath = os.path.dirname(os.path.abspath(__file__))
    fpath = os.path.join(fpath, 'data.json')

    fhandler = open(fpath, 'r')
    data = json.load(fhandler)
    fhandler.close()

    return data


def get_data_as_list():
    """Returns the stored data as a list object.

    Returns:
        list: A list of serialized data.

    Examples:
        >>> get_data_as_list()
        [578, 389, ...]
    """
    return get_raw_data()


def get_data_as_tuple():
    """Returns the stored data as a tuple.

    Returns:
        tuple: A tuple of serialized data.

    Examples:
        >>> get_data_as_tuple()
        (578, 389, ...)
    """
    return tuple(get_raw_data())


def get_nested_data():
    """Returns the stored data as a nested sequence.

    Returns:
        list: A list of tuples.

    Examples:
        >>> get_nested_data()
        [(578, 389), ...]
    """
    retval = []
    tupval = ()
    for idx, value in enumerate(get_raw_data()):
        if idx % 2:
            tupval = (value,)
        else:
            tupval += (value,)
            retval.append(tupval)

    return retval
