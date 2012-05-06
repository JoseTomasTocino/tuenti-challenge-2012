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

def main():
    for line in sys.stdin:
        elements = filter(None, line.strip().split())

        res = 0
        operands = []

        for e in elements:

            # Forth programming language
            
            try:
                n = int(e)
                operands.append(n)
                continue
            except ValueError:
                pass
            
            if e == ".":
                print operands.pop()

            # Cambio de signo
            elif e == "mirror":
                n = operands.pop()
                operands.append(-n)
            
            # Duplicar operando
            elif e == "breadandfish":
                operands.append(operands[-1])

            # Rechazar operando
            elif e == "fire":
                operands.pop()

            # Cambiar orden de los dos últimos operandos
            elif e == "dance":
                n1 = operands.pop()
                n2 = operands.pop()

                operands.append(n1)
                operands.append(n2)

            # Módulo
            elif e == "conquer":
                n1 = operands.pop()
                n2 = operands.pop()

                operands.append(n2 % n1)

            # Resta
            elif e == "$":
                n1 = operands.pop()
                n2 = operands.pop()

                operands.append(n2 - n1)

            # División
            elif e == "&":
                n1 = operands.pop()
                n2 = operands.pop()

                operands.append(n2 / n1)

            # Suma
            elif e == "@":
                n1 = operands.pop()
                n2 = operands.pop()

                operands.append(n2 + n1)

            # Producto
            elif e == "#":
                n1 = operands.pop()
                n2 = operands.pop()

                operands.append(n2 * n1)



if __name__ == '__main__':
    main()
