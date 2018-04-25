#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""A simple rock, paper, scissors game."""


import random


GAMEOPTIONS = ['rock', 'paper', 'scissors']
USERCHOICE = raw_input('Rock, paper, or scissors? ').lower()
AICHOICE = random.choice(GAMEOPTIONS)
RESULT = 'The computer chose [{}]!'.format(AICHOICE)
BADCHOICE = ("Sorry, that\'s not an option.\n"
             "Please try again with: [rock, paper, or scissors]\n")
WINNER = 'You win!'
DRAW = 'It\'s a draw!'
LOSS = 'Sorry, you lost. Better luck next time!'


while USERCHOICE not in GAMEOPTIONS:
    print BADCHOICE
    newchoice = raw_input('Rock, paper, or scissors? ').lower()
    if newchoice in GAMEOPTIONS:
        USERCHOICE = newchoice


if USERCHOICE == 'rock' and AICHOICE == 'scissors':
    print RESULT + '\n' + WINNER
elif USERCHOICE == 'paper' and AICHOICE == 'rock':
    print RESULT + '\n' + WINNER
elif USERCHOICE == 'scissors' and AICHOICE == 'paper':
    print RESULT + '\n' + WINNER
elif USERCHOICE == AICHOICE:
    print RESULT + '\n' + DRAW
else:
    print RESULT + '\n' + LOSS
