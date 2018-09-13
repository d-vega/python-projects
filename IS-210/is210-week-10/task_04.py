#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Merging dictionary data"""


import data


NICKS = data.BANDS['Buckingham Nicks'] = {
    'Lindsey Buckingham': ['guitar', 'vocals'],
    'Stevie Nicks': ['vocals', 'tambourine']
    }


data.BANDS['Fleetwood Mac'].update(NICKS)
