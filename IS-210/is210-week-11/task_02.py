#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Creating my own class from the ground-up"""


import time


class Snapshot(object):
    """An object storing time of Snapshot information."""

    def __init__(self, created=time.time()):
        """Constructor for Snapshot class.

        Args:
            created (mixed): By default it will return the current Unix
                Timestamp.

        Attributes:
            created (int): Will display the current Unix Timestamp as a floating
                integer.
        """
        self.created = created
        return
