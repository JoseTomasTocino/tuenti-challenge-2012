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
from numpy import *

def main():

    # From binary to string to ascii string
    binToAscii = lambda x : "".join([chr(int("".join(x[i:i+8]), 2)) for i in range(0, len(x), 8)])

    
    R = array([[0,0,1,0,0,0,0],
              [0,0,0,0,1,0,0],
              [0,0,0,0,0,1,0],
              [0,0,0,0,0,0,1]])

    # Parity check matrix
    H = array([[1,0,1,0,1,0,1],
              [0,1,1,0,0,1,1],
              [0,0,0,1,1,1,1]])

    # For each case
    for c in sys.stdin:

        # Strip the line
        c = c.strip()

        try:
            message = ""

            # Go in chunks of 7 bits
            for i in range(0, len(c), 7):

                # Get the chunk of 7 bits
                chunk = map(int, c[i:i+7])

                # Get the erroneous bit matrix
                errors = dot(H, chunk)

                # Get the index of the erroneous bit
                errBit = int("".join(map(str, list(errors % 2)[::-1])),2) - 1

                # Swap that motherfucker!
                if errBit:
                    chunk[errBit] = 1 - chunk[errBit]

                # Compute the result
                data_chunk = list(dot(R, chunk))

                # Add it to the message
                message += "".join(map(lambda x: str(int(x)), data_chunk))

            asciiMessage = binToAscii(message)
            asciiNums = [ord(x) for x in asciiMessage]

            if min(asciiNums) < 32 or max(asciiNums) > 126:
                print "Error!"
            else:
                print asciiMessage
            

        except ValueError:
            print "Error!"



if __name__ == '__main__':
    main()
