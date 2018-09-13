#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Final exam - Programming project"""


from itertools import cycle, islice


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
    """Pass in the entire player list of attendees who want to participate in
    the competition. This function will filter out the bad connections then
    assign players to teams in round robin fashion.

    Args:
        players (list): The players should be in list format with tuples
            inside representing the username and connectivity they have, i.e.
            ('username', 1)
        teams (int, optional): The max number of teams participating.
        min_team (int, optional): The minimum number of players required per
            team assignment.
        max_team (int, optional): The maximum number of players allowed per team
            assignment.

    Returns:
        list: The team assignments will be returned in a list format filtered
            by connectivity, ensuring each team faces off a player they have not
            played against before.

    Examples:

        >>> people = [('a', 1), ('b', 0), ('c', 1), ('d', 1), ('e', 1),
        ('f', 1)]
        >>> print matchmaking(people, teams=2, min_team=1, max_team=2)
        [['a', 'd'], ['c', 'e']]

        >>> import data
        >>> print matchmaking(data.userdat, teams=4, min_team=1, max_team=5)
        [['xxjackson_is_backson', 'apples_to_apples', 'HappyFarer127',
        'Edge_Lord_020', 'porosnaxx'], ['sammy-is-here-679', 'heyharambe',
        'ParisInca', 'blueskies123', 'WeaverZin'], ['TabChoose', 'MaxiZollo',
        'dark_shadow89', 'Wickedryva', 'GreatBeardling'], ['EditPassion',
        'pootismylootis', 'crosidco', 'iAmTheWebz', 'Cookineta']]
        """

    def assignments(player_list):
        """Players that have already been filtered out by connection will
        initially be assigned a team in this function. If there is an empty
        team or not enough players on a team, the function will return False.

        Args:
            player_list (list): This will be the already filtered player list
            by good connection type.

        Returns:
            list: A list of team assignments will be returned according to
                number of teams specified in the arguments. It will later be
                reassembled according to round robin fashion.
        """
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
