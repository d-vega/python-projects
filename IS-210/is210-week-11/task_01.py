#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Instantiating and accessing custom class instances"""


import produce


TOMATO = produce.Produce()
TOMATO_ARRIVAL = TOMATO.arrival
EGGPLANT = produce.Produce(1311210802)
EGGPLANT_EXPIRES = EGGPLANT.get_expiration()
