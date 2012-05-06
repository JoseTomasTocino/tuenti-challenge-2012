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
from math import ceil

def main():
    numCases = int(sys.stdin.readline())

    for currentCase in range(numCases):
        width, height, count = map(int, filter(None, sys.stdin.readline().strip().split()))
        listOfWords = sys.stdin.readline().strip().split()

        # Width and height measured in stitches
        widthSt = width * count
        heightSt = height * count

        maxSize = 0.
        spaces = 0

        # The absolute maximum for the font size will be min(width, height)
        for currentFontSize in reversed(range(min(widthSt, heightSt) + 1)):

            cantFit = False
            remainingHorSpace = widthSt
            remainingVerSpace = heightSt

            currentLine = ""

            for currentWord in listOfWords:

                # Get the width of the current word
                currentWordWidth = len(currentWord) * currentFontSize

                # If the word does not fit alone in a line, we can't use this font size
                if currentWordWidth > widthSt:
                    cantFit = True
                    break

                # Plausible font size
                else:
                    
                    # First word of first
                    if currentLine == "":

                        # Reduce the remaining horizontal space
                        remainingHorSpace -= currentWordWidth

                        # Reduce the remaining vertical space
                        remainingVerSpace -= currentFontSize
                    
                        # Add the word to the line
                        currentLine = currentWord

                    # Not the first of the line, but there's room for it
                    elif remainingHorSpace >= (currentWordWidth + currentFontSize):

                        # Reduce the remaining horizontal space (space + word)
                        remainingHorSpace -= currentFontSize + currentWordWidth    

                        # Update the string for the current line
                        currentLine += " " + currentWord

                    # No room in the current line, but there's space in the next
                    elif remainingVerSpace >= currentFontSize:

                        # Reset the horizontal space var
                        remainingHorSpace = widthSt - currentWordWidth

                        # Decrease the vertical space
                        remainingVerSpace -= currentFontSize

                        # Restart the string that holds the text for the line
                        currentLine = currentWord

                    # OMG there's no where to go
                    else:                        
                        cantFit = True
                        break

            if not cantFit:

                # Get the amount of characters
                numberOfCharacters = len("".join(listOfWords))

                # Calculate the inches per thread
                inchesOfThreadPerStitch = 1. / count

                # Calculate the stitches per character
                stitchesPerCharacter = (currentFontSize * currentFontSize) / 2.

                # Output the result
                print "Case #%i:" % (currentCase + 1), int(ceil(numberOfCharacters * stitchesPerCharacter * inchesOfThreadPerStitch))

                break

if __name__ == '__main__':
    main()
