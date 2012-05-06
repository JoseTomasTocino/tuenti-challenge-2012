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
import base64
import math
import binascii
import itertools

def neg(n,w):
    b = 0
    if type(n) is int:
        b = list(bin(n)[2:].zfill(w))
    else:
        b = list(n.zfill(w))

    b.reverse()
    
    p = 0
    inverting = False

    for i,c in enumerate(b):
        if not inverting and c == '1':
            inverting = True
        elif inverting:
            b[i] = '0' if c == '1' else '1'

    b = b[:w]
    b.reverse()

    return "".join(b)


def getCommon(s):
    n = 0
    for c in itertools.izip(*s):
        n += 1 if len(set(c)) == 1 else 0

    return s[0][:n]

def main():
    # Read the data
    in_str = sys.stdin.readline()

    # Decode the base64
    in_b64 = base64.b64decode(in_str)

    # Turn each hexadecimal character in a 4-long binary digit and join em all
    in_bin = "".join([bin(int(x,16))[2:].zfill(4) for x in in_b64])

    # Split the binary input in 32bit chunks
    chunks = [in_bin[i:i+32] for i in range(0, len(in_bin), 32)]

    # Find the common part in all the chunks
    common_part = getCommon(chunks)
    common_part_length = len(common_part)

    # Create a vector of stripped chunks
    s_chunks = [x[common_part_length:] for x in chunks]

    # Init the string for the compressed output
    compressed_output = ""

    # Repeating pattern
    init_pattern = "1" + common_part

    # Counter
    i = 0
    j = 0

    # It's 05:56, i'm tired of adding comments

    while i < len(s_chunks) - 1:
        current_chunk = s_chunks[i]
        current_number = int(current_chunk, 2)

        #print current_number

        compressed_output += init_pattern + current_chunk
        j = i + 1

        seen_numbers = []

        local_add = ""

        while j < len(s_chunks):
            next_chunk = s_chunks[j]
            next_number = int(next_chunk, 2)

            difference = next_number - current_number

            if next_number in seen_numbers:
                break

            if difference >= -16 and difference <= 15:
                seen_numbers.append(difference)
                bin_dif = ""
                if difference < 0:
                    bin_dif =  "0" + neg(difference, 5)
                else:
                    bin_dif += bin(difference)[2:].zfill(6)

                #print "  ", next_number, "(",difference, "-", bin_dif,")"

                current_number = next_number
                compressed_output += bin_dif
                local_add += bin_dif
            else:
                break

            j += 1
            i += 1

        i += 1

    if i < len(s_chunks):        
        current_chunk = s_chunks[i]
        current_number = int(current_chunk, 2)

        compressed_output += init_pattern + current_chunk

    compressed_output += "0"

    hex_final_chars = "".join([hex(int(compressed_output[n:n+4],2))[2:] for n in range(0, len(compressed_output), 4)])
    z = list(base64.b64encode(hex_final_chars))
    while z[-1] == "=":
        z.pop()
    print "".join(z)
    

if __name__ == '__main__':
    main()

