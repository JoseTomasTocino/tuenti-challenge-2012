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

import sys
import itertools
from fractions import gcd

def alternate(s1, s2): 
    for e1, e2 in itertools.izip_longest(s1, s2): 
        yield e1; 
        yield e2;

# This is from http://www.enrico-franchi.org/2010/09/nice-functional-lcm-in-python.html
def lcm(numbers):
    return reduce(lambda x, y: (x*y)/gcd(x,y), numbers, 1)

def main():

    # Get the number of cases
    numCases = int(sys.stdin.readline().strip())

    # For each case
    for case in range(numCases):

        # Read the input
        numCards, num1 = map(int, filter(None, sys.stdin.readline().strip().split()))

        # Deck of cards
        initialDeck = list(range(1, numCards + 1))

        # Divide the deck
        firstDeck = initialDeck[:num1]
        secondDeck = initialDeck[num1:]

        # Reverse the subdecks
        firstDeck.reverse()
        secondDeck.reverse()
  
        # Initialise the shuffle deck
        shuffleDeck = []

        for c in alternate(firstDeck, secondDeck):
            if c:
                shuffleDeck.append(c)

        # Make pairs between the original the deck elements and the elements in the shuffle deck
        pairs = dict(zip(initialDeck, shuffleDeck))

        # Reset the counter
        i = 0

        # Container for the groups
        groups = []

        while len(pairs) != 0:

            # Get the first pair
            e = pairs.popitem()

            s = 1

            if e[0] == e[1]:
                i += 1
                continue
            
            # Save the initial element
            oe = e[0]
            fe = e[1]

            while 1:

                # Pick a pair with the second element as the first element of the previous
                ne = pairs[fe]
                
                # Get that pair out of the original group
                pairs.pop(fe)

                # Increase the number of the group
                s += 1

                if ne == oe:
                    break
                else:
                    fe = ne

            groups.append(s)
            i += 1

        print "Case #%i:" % (case + 1), lcm(groups)
        

if __name__ == '__main__':
    main()
