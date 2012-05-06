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
import png

def main():

    # Open the image
    r = png.Reader("/home/jose/Dropbox/tuenti/p12/CANTTF.png")

    # Read the image
    rr = r.read()

    # Get the pixel set
    pixels = rr[2]

    # Get the first Row
    fR = pixels.next()

    # initialise the bit set
    bitSet = ""

    # Initialise counter
    i = 0

    # Start fetching bits
    while 1:
        
        # Get each channel value
        r,g,b = fR[i], fR[i + 1], fR[i + 2]

        # Get the LSB of each channel
        r = bin(r)[-1]
        g = bin(g)[-1]
        b = bin(b)[-1]

        # Insert those LSBs in the bitset

        bitSet += r
        i += 1
        if i == 256: break

        bitSet += g
        i += 1
        if i == 256: break

        bitSet += b
        i += 1
        if i == 256: break
        

    s3 = ""
    for i in range(0,256,8):
        c = bitSet[i:i+8]
        s3 += chr(int(c, 2))

    # From the PNG comments
    s1 = "a541714a17804ac281e6ddda5b707952"

    # From the QR code
    s2 = "ed8ce15da9b7b5e2ee70634cc235e363"

    if 0:
        print s1
        print s2
        print s3

    k1 = map(lambda x: int(x, 16), list(s1))
    k2 = map(lambda x: int(x, 16), list(s2))
    k3 = map(lambda x: int(x, 16), list(s3))

    for line in sys.stdin:
        k4 = map(lambda x: int(x, 16), list(line.strip()))

        u = zip(k1,k2,k3,k4)
        r = [hex((x[0] + x[1] + x[2] + x[3]) % 16)[2:] for x in u]

        print "".join(r)

if __name__ == '__main__':
    main()
