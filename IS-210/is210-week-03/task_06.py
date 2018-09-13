#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""A very long book."""

import os

DPATH = os.path.dirname(os.path.abspath(__file__))

FHANDLER = open(os.path.join(DPATH, 'war_and_peace.txt'), 'r')

WORDS = FHANDLER.read()

FHANDLER.close()

WORDCT = len(WORDS.split())
