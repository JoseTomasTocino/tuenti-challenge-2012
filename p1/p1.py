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


matrix = [["","",""] for i in range(4)]

matrix [0][0] = " 1";
matrix [0][1] = "ABC2";
matrix [0][2] = "DEF3";
matrix [1][0] = "GHI4";
matrix [1][1] = "JKL5";
matrix [1][2] = "MNO6";
matrix [2][0] = "PQRS7";
matrix [2][1] = "TUV8";
matrix [2][2] = "WXYZ9";
matrix [3][0] = "";
matrix [3][1] = "0";

timeMoveVertical = 300
timeMoveHorizontal = 200
timeMoveDiagonal = 350
timePress = 100
timeRepeat = 500

def findPos (c):
    for i1, sublist in enumerate(matrix):
        for i2, characters in enumerate(sublist):
            if c.upper() in characters:
                return (i1, i2)

    return (-1,-1)

def computePath(current, target):
    mH, mV, mD, mR = [0,0,0,0]

    currentVer, currentHor = current
    targetVer, targetHor = target

    difHor = abs(targetHor - currentHor)
    difVer = abs(targetVer - currentVer)

    # Same character
    if difHor == 0 and difVer == 0:
        mR = 1

    elif difHor == 0 and difVer != 0:
        mV = 1
        currentVer += 1 if currentVer < targetVer else -1

    elif difVer == 0 and difHor != 0:
        mH = 1
        currentHor += 1 if currentHor < targetHor else -1

    else:
        mD = 1
        currentVer += 1 if currentVer < targetVer else -1
        currentHor += 1 if currentHor < targetHor else -1

    if currentHor != targetHor or currentVer != targetVer:
        mH2, mV2, mD2, mR2 = computePath((currentVer, currentHor), target)
        return (mH + mH2, mV + mV2, mD + mD2, mR + mR2)
    else:
        return (mH, mV, mD, mR)

def calcDelta(current, target):
    delta = 0

    currentVer, currentHor = current
    targetVer, targetHor = target

    mH, mV, mD, mR = computePath((currentVer, currentHor), (targetVer, targetHor))

#    print "From", current, "to", target, ":"
#    print "mH", mH, "mV", mV, "mD", mD, "mR", mR

    delta += mH * timeMoveHorizontal
    delta += mV * timeMoveVertical
    delta += mD * timeMoveDiagonal
    delta += mR * timeRepeat

    return delta

def main():

    capsLockHor = 2;
    capsLockVer = 3;

    numCases = int(sys.stdin.readline())
    
    for c in range(numCases):
        currentString = sys.stdin.readline().strip()

        acumTime = 0

        currentHor = 1;
        currentVer = 3;

        capsEnabled = False

        for currentCharacter in currentString:
            # If we need to switch caps lock
            if (currentCharacter.isupper() and not capsEnabled) or (currentCharacter.islower() and capsEnabled):
                capsEnabled = not capsEnabled
                acumTime += calcDelta ((currentVer, currentHor), (capsLockVer, capsLockHor))
                acumTime += timePress
                currentVer, currentHor = capsLockVer, capsLockHor

            targetVer, targetHor = findPos(currentCharacter.upper())

#            print
#            print "Current position: ", (currentVer, currentHor)
#            print "Current character: '" + currentCharacter + "'"
#            print "Character position: ", (targetVer, targetHor)

            acumTime += calcDelta ((currentVer, currentHor), (targetVer, targetHor))
            acumTime += timePress * (matrix[targetVer][targetHor].index(currentCharacter.upper()) + 1)

            currentVer, currentHor = targetVer, targetHor

        print acumTime
        acumTime = 0


if __name__ == '__main__':
    main()
