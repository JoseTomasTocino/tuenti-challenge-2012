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

threshold = 0.5
learning_rate = 0.1
training_set = [((1, 0, 0), 1), ((1, 0, 1), 1), ((1, 1, 0), 1), ((1, 1, 1), 0)]

def sum_function(values, weights):
    return sum(value * weights[index] for index, value in enumerate(values))

def main():

    numKnownRep   = int(sys.stdin.readline())
    numUnknownRep = int(sys.stdin.readline())
    numTotalCalls = int(sys.stdin.readline())

    baseCases = []
    newCases  = []

    # For each known case
    for i in range(numKnownRep):

        # Read the case
        V = filter(None, sys.stdin.readline().strip().split())
        S = 1 if V[0] == "S" else 0
        V = map(int, V[1:])

        # Add it to the base of knowledge
        baseCases.append( (S, V) )
    
    # For each unknown case
    for i in range(numUnknownRep):

        # Read the case
        V = map(int, filter(None, sys.stdin.readline().strip().split()))

        # Add it to the base of knowledge
        newCases.append( V )
        

    # Perceptron from http://en.wikipedia.org/wiki/Perceptron
    weights = [0] * numTotalCalls

    while True:
        error_count = 0

        for desired_output, input_vector in baseCases:
            result = 1 if sum_function(input_vector, weights) > threshold else 0
            error = desired_output - result
            if error != 0:
                error_count += 1
                for index, value in enumerate(input_vector):
                    weights[index] += learning_rate * error * value
        if error_count == 0:
            break

    sss = 0
    for c in newCases:
        if sum(map(lambda x : x[0] * x[1], zip(c,weights))) < 0:
            sss += sum(c)

    print sss

if __name__ == '__main__':
    main()
