#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Practicing with comprehensions"""


from data import FRUIT


def get_cost_per_item(shoplist):
    """Get the cost per-item in your shopping list.

    Args:
        shoplist(dict): Your input should be a dictionary shopping list for this
            function to work.

    Returns:
        dict: The resulting dictionary will reflect each item in the original
            dict with the cost per0item.

    Examples:
        >>> get_cost_per_item({'Lime': 12, 'Red Pear': 4, 'Peach': 24,
        'Beet': 1})
        {'Lime': 7.08, 'Peach': 95.76, 'Red Pear': 9.96}

        >>> get_cost_per_item({'Granny Smith Apple': 2, 'Forelle Pear': 3,
        'Blueberries': 4})
        {'Forelle Pear': 8.97, 'Blueberries': 15.96, 'Granny Smith Apple': 3.98}
    """
    newdict = {k: int(shoplist[k])*FRUIT[k] for k in shoplist if k in FRUIT}
    return newdict


def get_total_cost(shoplist):
    """Get the total cost of fruits to be purchased.

    Args:
        shoplist(dict): The input needs to be a dictionary in order to work.

    Returns:
        float: The resulting number is a float value of the total cost of fruits
            to be purchased.

    Examples:
        >>> get_total_cost({'Granny Smith Apple': 2, 'Forelle Pear': 3,
        'Blueberries': 4})
        28.91

        >>> get_total_cost({'Lime': 12, 'Red Pear': 4, 'Peach': 24, 'Beet': 1})
        112.80000000000001
    """
    dict1 = get_cost_per_item(shoplist)
    itm_cst = dict1.values()
    result = sum(itm_cst+[shoplist[k] for k in shoplist.iteritems()
                          if k in FRUIT])
    return result
