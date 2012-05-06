#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (C) 2011 José Tomás Tocino García <theom3ga@gmail.com>

# Autor: José Tomás Tocino García

# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA
# 02110-1301, USA.

import sys, copy
from pprint import pprint

def removeFromLeft (nbr, e):
    for k in nbr:
        nbr[k][0].discard(e)

def main():

    nbr = {}

    for line in sys.stdin:

        l,c,r = list(line.strip())

        for k in [l,c,r]:
            if k not in nbr: nbr[k] = [set(),set()]

        nbr[l][1].add(c)
        nbr[l][1].add(r)

        nbr[c][0].add(l)
        nbr[c][1].add(r)

        nbr[r][0].add(l)
        nbr[r][0].add(c)

    # Now I need to get the characters with empty left neighbors
    lefters = [x for x in nbr if len(nbr[x][0]) == 0]

    possiblePasswords = set()

    for l in lefters:
        possiblePasswords.update(buildString(nbr, l))

    sortedPasswords = sorted(list(possiblePasswords))
    for p in sortedPasswords:
        print p


def buildString (original_nbr, l):

    stringRests = set()

    nbr = copy.deepcopy(original_nbr)

    # Remove the letter from the dict
    del nbr[l]

    # Remove the letter of the left neighbors of all characters
    removeFromLeft(nbr, l)

    # Now I need to get the characters with empty left neighbors
    emptyLeft = [x for x in nbr if len(nbr[x][0]) == 0]

    if not emptyLeft:
        return set(l)
    else:
        for c in emptyLeft:
            stringRests.update(buildString(nbr, c))

        returnValue = set()
        for c in stringRests:
            returnValue.add(l + c)

        return returnValue
        



if __name__ == '__main__':
    sys.setrecursionlimit(25)
    main()
