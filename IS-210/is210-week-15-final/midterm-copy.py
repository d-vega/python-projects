#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Final exam - Programming project"""


from itertools import cycle, islice
from data import userdat


def roundrobin(*iterables):
    "roundrobin('ABC', 'D', 'EF') --> A D E B F C"
    # Generator Recipe credited to George Sakkis (From Built-in Library)
    pending = len(iterables)
    nexts = cycle(iter(it).next for it in iterables)
    while pending:
        try:
            for next in nexts:
                yield next()
        except StopIteration:
            pending -= 1
            nexts = cycle(islice(nexts, pending))


def matchmaking(players, teams=3, min_team=1, max_team=None):
    """Main function docstring"""

    def assignments(player_list):
        """Second nested function """
        teams_list = [[] for _ in xrange(teams)]
        ttl_plyrs = len(player_list) / teams
        counter = 0

        try:
            for member in range(0, len(player_list), max_team):
                team = player_list[member:member+max_team]
                if len(teams_list[counter]) != min_team:
                    teams_list[counter].extend(team)
                counter += 1

            for member in xrange(len(teams_list)):
                if teams_list[member] == []:
                    return False

        except IndexError:
            pass

        except TypeError:
            try:
                for member in range(0, len(player_list)):
                    team = player_list[member:member+ttl_plyrs]
                    if len(teams_list[counter]) != min_team:
                        teams_list[counter].extend(team)
                    counter += 1

            except IndexError:
                pass
        return teams_list


    player_names = []

    for user in players:
        if user[1] == 1:
            player_names.append(user[0])

    player_list = assignments(player_names)
    contestants = assignments(list(roundrobin(*player_list)))


    for team in xrange(len(contestants)):
        chk_teams = len(contestants[team]) < min_team
        if contestants[team] == [] or chk_teams:
            return False

    return contestants



people = [('a', 1), ('b', 0), ('c', 1), ('d', 1), ('e', 1), ('f', 1)]
print matchmaking(people, teams=1, min_team=1, max_team=1)
print matchmaking(people, teams=2, min_team=1, max_team=1)
print matchmaking(people, teams=2, min_team=1, max_team=2)
print matchmaking(people, teams=2, min_team=3)
print matchmaking(people, teams=6, min_team=1)
print matchmaking(people, teams=1, min_team=1)
print matchmaking(userdat, teams=4, min_team=1, max_team=5)
