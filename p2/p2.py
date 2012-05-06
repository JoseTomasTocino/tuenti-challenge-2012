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

def countOnes(n):
    return bin(n)[2:].count('1')

def main():
    c = 1
    numCases = sys.stdin.readline()
    for line in sys.stdin:
        n = int(line.strip())
        pairs = []

        maxOnes = 0

        for i in range(n):
            sumOfOnes = countOnes(i) + countOnes(n - i)
            if sumOfOnes > maxOnes:
                maxOnes = sumOfOnes
                         
        print "Case #" + str(c) + ": " + str(maxOnes)
        c += 1

if __name__ == '__main__':
    main()
