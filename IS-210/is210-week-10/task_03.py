#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Adding and removing keys to Python dictionaries"""


import data


CORRECTED = data.BANDS.copy()
CORRECTED['Dylan'] = {'Bob Dylan': ['vocals', 'guitar', 'harmonica']}


del CORRECTED['Van Halen']['David Lee Roth']


CORRECTED['Van Halen']['Sammy Hagar'] = ['vocals']
