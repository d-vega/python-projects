#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Check your systolic blood pressure"""


PATIENT_INPUT = int(raw_input('What is your blood pressure? '))
LOW_BP = PATIENT_INPUT < 90
IDEAL_BP = PATIENT_INPUT >= 90 and PATIENT_INPUT <= 119
WARN_BP = PATIENT_INPUT >= 120 and PATIENT_INPUT <= 139
HIGH_BP = PATIENT_INPUT >= 140 and PATIENT_INPUT <= 159
# EMERG_BP = PATIENT_INPUT >= 160

if IDEAL_BP:
    BP_STATUS = 'Ideal'
elif LOW_BP:
    BP_STATUS = 'Low'
elif HIGH_BP:
    BP_STATUS = 'High'
elif WARN_BP:
    BP_STATUS = 'Warning'
else:
    BP_STATUS = 'Emergency'


print 'Your status is currently: {}'.format(BP_STATUS)
