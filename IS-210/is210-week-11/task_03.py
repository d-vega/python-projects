#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Practicing with subclasses"""


import produce


class Apple(produce.Produce):
    """An object storing produce information on Apples."""

    def __init__(self):
        """Constructor for Apple class. Explicitly inherits from another class
        already."""
        produce.Produce.__init__(self)
        return


Apple.duration = 5356800
