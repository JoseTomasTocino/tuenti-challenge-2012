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
import datetime

ledsPerNumber = [6,2,5,5,4,5,6,3,7,6]

ledChanges = {}
for i in range(10):
    ledChanges["%d-%d" % (i,i)] = 0

ledChanges['0-1'] = 0	
ledChanges['1-2'] = 4	
ledChanges['2-3'] = 1
ledChanges['3-4'] = 1
ledChanges['4-5'] = 2
ledChanges['5-6'] = 1	
ledChanges['6-7'] = 1	
ledChanges['7-8'] = 4
ledChanges['8-9'] = 0
ledChanges['9-0'] = 1
ledChanges['5-0'] = 2 
ledChanges['2-0'] = 2 
ledChanges['3-0'] = 2

one_second = datetime.timedelta(seconds = 1)

jump = True

############################################################
# OLD CLOCK
############################################################

def calcOld (t1, t2):

    leds = 0

    leds += 36

    if jump:
        dif = t2 - t1
        leds += 2401920 * dif.days
        t1 += datetime.timedelta(days = dif.days)

    while t1 < t2:
        t1 += one_second
        localDelta = countLedsTime(t1)
        leds += localDelta

    return leds

def countLedsTime(t):
    """ Count the active leds for a given time"""
    ledCount = 0
    
    ledCount += countLedsInDigit(t.hour)
    ledCount += countLedsInDigit(t.minute)
    ledCount += countLedsInDigit(t.second)

    return ledCount

def countLedsInDigit(p):
    """ Count the active leds for a number with two digits"""
    ledCount = 0

    # Convert the given number to a string representation with two digits
    pStr = "%02d" % p

    firstDigit = int(pStr[0])
    secondDigit = int(pStr[1])

    ledCount = ledsPerNumber[firstDigit] + ledsPerNumber[secondDigit]

    return ledCount


############################################################
# NEW CLOCK
############################################################

def timeToListOfNumbers(t):    
    """ Receives a time and returns a list with the digits of that time
    For example, for a datetime with the time 14:52:50, it would return
    
    [1,4,5,2,5,0]

    """
    #return map(int, list("%02d%02d%02d" % (t.hour, t.minute, t.second)))
    return list("%02d%02d%02d" % (t.hour, t.minute, t.second))


def countLedsDiff(t1, t2):
    """ Counts how many leds change from one time to another"""

    numChanges = 0

    # Get list of digits
    numT1 = timeToListOfNumbers(t1)
    numT2 = timeToListOfNumbers(t2)

    assert len(numT1) == 6
    assert len(numT2) == 6

    for i in range(6):
        numChanges += ledChanges[numT1[i] + "-" + numT2[i]]

    #numChanges = sum(map(lambda x,y: ledChanges[x][y], numT1, numT2))
    return numChanges

def calcNew (t1, t2):

    leds = 0

    leds += 36

    if jump:
        dif = t2 - t1
        leds += 146443 * dif.days
        t1 += datetime.timedelta(days = dif.days)

    while t1 < t2:
        localDelta = countLedsDiff(t1, t1 + one_second)
        leds += localDelta
        t1 += one_second

    return leds

########################################
# MAIN
########################################

def stringToDate (s):
    """ Converts a string with the format '2012-01-18 00:00:00' to a datetime object"""
    p = datetime.datetime.strptime(s, '%Y-%m-%d %H:%M:%S')
    return p

def main():

    # For each case
    for line in sys.stdin:

        # Ignore comments starting with #
        if line[0] == '#':
            continue

        # Split the line in two strings
        leftString, rightString = line.strip().split(" - ")

        # Convert those two strings to datetime objects
        leftTime, rightTime = stringToDate(leftString) , stringToDate(rightString)

        # Calculate the amount of leds turned on by the old clock
        oldLeds = calcOld(leftTime, rightTime)

        # Calculate the amount of leds turned on by the new clock
        newLeds = calcNew(leftTime, rightTime)

        print (oldLeds - newLeds)
        

if __name__ == '__main__':
    main()

