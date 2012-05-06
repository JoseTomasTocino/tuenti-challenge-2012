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
import pprint
import itertools

def main():

    scores = {}
    scores['A'] = 1
    scores['B'] = 3
    scores['C'] = 3
    scores['D'] = 2
    scores['E'] = 1
    scores['F'] = 4
    scores['G'] = 2
    scores['H'] = 4
    scores['I'] = 1
    scores['J'] = 8
    scores['K'] = 5
    scores['L'] = 1
    scores['M'] = 3
    scores['N'] = 1
    scores['O'] = 1
    scores['P'] = 3
    scores['Q'] = 10
    scores['R'] = 1
    scores['S'] = 1
    scores['T'] = 1
    scores['U'] = 1
    scores['V'] = 4
    scores['W'] = 4
    scores['X'] = 8
    scores['Y'] = 4
    scores['Z'] = 10

    f = open("/home/jose/Dropbox/tuenti/p11/descrambler_wordlist.txt", "r")
    words = map(lambda x: x.strip(), f.readlines())
    f.close()

    wordsCache = {}

    for c in list("abcdefghijklmnopqrstuvwxyz".upper()):
        wordsCache[c] = {}
        for s in range(1,25):
            wordsCache[c][s] = [x for x in words if c in x and len(x) == s]


    biggerWordsCache = {}

    # Read number of cases
    numCases = int(sys.stdin.readline().strip())

    # For each case
    for case in range(numCases):

        # Read the letters in the rack, and the word in the board
        letters, word = map(None, sys.stdin.readline().strip().split())

        # Set for the global possible words
        possibleWords = set()

        # Let's generate all the possible subsets of the letters of the rack
        # For each possible size of subset
        for numLettersPicked in range(1, len(letters) + 1):

            #print "Subsets of size %i" % numLettersPicked

            # Generate all the subsets of size numLetterPicked
            for subletters in itertools.combinations(letters, numLettersPicked):
                
                # For each letter of the word in the board
                for l1 in word:
                    availableLetters = []
                    availableLetters.append(l1)
                    availableLetters.extend(subletters)
                    availableLetters.sort()
                    availableLetterStr = "".join(availableLetters)

                    numAvLetters = len(availableLetters)

                    realWords = []

                    if availableLetterStr in biggerWordsCache:
                        realWords = biggerWordsCache[availableLetterStr]

                    else:
                        # Set of words with the letter l1
                        stlist = wordsCache[l1.upper()][numAvLetters][:]    

                        # Intersect the previous set with those with the chosen letters
                        for l2 in subletters:
                            stlist = [x for x in stlist if l2 in x]
                            #stlist.intersection_update(wordsCache[l2.upper()][numAvLetters])

                        # Get only the words that use all and only the available letters
                        realWords = [x for x in stlist if sorted(x) == availableLetters]

                        biggerWordsCache[availableLetterStr] = realWords

             
                    # Compute the scores of these words and add them to the general set
                    for plWord in realWords:
                        possibleWords.add((sum([scores[x] for x in plWord]), plWord))

        # Sort the words by score
        sortedWords = sorted(list(possibleWords), key = lambda x: x[0], reverse = True)

        # Get the highest score
        highestScore = sortedWords[0][0]

        # Get the words with the highest score (if more than one)
        highestWords = sorted([x[1] for x in sortedWords if x[0] == highestScore])

        # Print the result
        print highestWords[0], highestScore
            

if __name__ == '__main__':
    main()
