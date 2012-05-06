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
import re

def main():
    numCases = int(sys.stdin.readline().strip())

    for currentCase in range(numCases):
        #print "Case %i" % (currentCase + 1)
        word, ocurrence = filter(None, sys.stdin.readline().strip().split())

        word = word.lower()

        ocurrence = int(ocurrence)

        #print "Word %s\nOcurrence: %i" % (word, ocurrence)
        
        acumulated_ocurrences = 0

        found_document = -1
        found_line = -1
        found_word = -1
        
        regexp = re.compile("\\b" + word + "\\b")

        for d in range(1,801):
            #print "\nChecking document %04d for word '%s'" % (d, word)
            #print "Acumulated ocurrences so far: %i" % acumulated_ocurrences

            f = open('/home/jose/documents/' + ("%04d" % d), 'r') 

            lineNumber = 0

            bigStr = f.read()
            bigStr = bigStr.lower()
            averageCount = bigStr.count(word)

            if averageCount == 0:
                #print "Quick skip"
                continue

            times = len(regexp.findall(bigStr))
            
            if times < (ocurrence - acumulated_ocurrences):
                acumulated_ocurrences += times
                f.close()
                continue
            else:
                f.seek(0)

            found = False

            for line in f:
                #print "  Checking line number %i" % lineNumber

                lastPos = 0
                lineNumber += 1

                glob_result = regexp.finditer(line.lower())

                if glob_result:
                    for result in glob_result:

                        acumulated_ocurrences += 1
                        pos = result.start()

                        if acumulated_ocurrences == ocurrence:
                            found = True
                            found_word = len(line[:pos].split()) + 1
                            break
                        else:
                            lastPos = pos + 1

                if found:
                    break

            if found: 
                found_document = d
                found_line = lineNumber
                break

            f.close()

        print "%i-" % found_document + "%i-" % found_line + "%i" % found_word


if __name__ == '__main__':
    main()
