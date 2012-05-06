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
import math
from matplotlib import pyplot
from shapely.geometry import *
from descartes.patch import PolygonPatch

def getSide(a, b, c):
     return ((b[0] - a[0])*(c[1] - a[1]) - (b[1] - a[1])*(c[0] - a[0])) > 0

def getVertices (n, c, v):

    R = math.sqrt(math.pow(c[0] - v[0], 2.0) + 
                  math.pow(c[1] - v[1], 2.0))

    aDelta = 2 * math.pi / n

    a = math.atan2(v[1] - c[1], v[0] - c[0])

    V = [v]

    for i in range(1, n):
        x = c[0] + R * math.cos(a + 2 * math.pi * i / n)
        y = c[1] + R * math.sin(a + 2 * math.pi * i / n)

        V.append((x,y))

    return V


def main():
    numCases = int(sys.stdin.readline())

    for case in range(numCases):
        possible = True
        draw = False

        pyplot.clf()

        # Read Pizza's center and radius
        Cx, Cy, Cr = map(float, filter(None, sys.stdin.readline().strip().split()))

        # Read the number of ingredient types
        n_ingredient_types = int(sys.stdin.readline())

        ingredient_types = []
        ingredients = {}

        # For each type of ingredient
        for i in range(n_ingredient_types):

            # Read and parse the attributes
            ing_name, ing_sides, ing_amount = filter(None, sys.stdin.readline().strip().split())
            ing_sides, ing_amount = map(int, [ing_sides, ing_amount])

            # The key of the dict will be the name and the number of sides
            ing_key = (ing_name, ing_sides)

            # Add this type of ingredient to the set
            ingredient_types.append(ing_key)
            
            # Initalize the dict of ingredients
            if ing_key not in ingredients:
                ingredients[ing_key] = []

            # For each actual present ingredient
            for j in range(ing_amount):

                # Read center and vertex positions
                c_x, c_y, v_x, v_y = map(float, filter(None, sys.stdin.readline().strip().split()))
            
                # Compute the rest of vertices and add them to the ingredients set
                ingredients[ing_key].append(((c_x, c_y), getVertices(ing_sides, (c_x, c_y), (v_x, v_y))))
            
            # If the number of ingredients of this type is not even, there
            # cannot be an even partition, so break this
            if len(ingredients[ing_key]) % 2 != 0:
                possible = False
                break

        if not possible:
            print "Case #%i: FALSE" % (case + 1)
            continue

        # Create the circle for the pizza
        extCircle = Point(Cx, Cy).buffer(Cr)

        # List of polygons
        polys = []

        if draw:
            fig = pyplot.figure(1, figsize = (5,5), dpi = 90)
            ax = fig.add_subplot(111)
            ax.plot(Cx, Cy, 'o', color = "#ff0000", zorder = 1)
            ax.add_patch(PolygonPatch(extCircle, facecolor = "#ff0000", alpha = 0.3, zorder = 4))

        # For each Ingredient Type (it)
        for it in ingredients:

            # For each ingredient of type it
            for i in ingredients[it]:

                # Create a polygon for the ingredient
                P = Polygon(i[1])

                # Add the polygon to the set
                polys.append(P)

                if draw:
                    patch = PolygonPatch(P, facecolor="#6699cc", edgecolor = "#6699cc", alpha = 0.5, zorder = 2)
                    ax.add_patch(patch)
                    for v in i[1]:
                         ax.plot(v[0], v[1], 'o', color = '#999999', zorder = 1)


        # Set of non-intersecting lines
        possibleDivisions = []

        possible = False

        # Test different angles from 0 to 180, one angle at a time
        for ang in range (0, 180, 1):

            # Switch to radians
            ang = math.radians(ang)

            # Get the starting and ending point for the line
            P1 = (Cx + Cr * math.cos(ang), Cy + Cr * math.sin(ang))
            P2 = (Cx - Cr * math.cos(ang), Cy - Cr * math.sin(ang))

            # Build the line
            L = LineString([P1, P2])

            # Intersection flag
            intersects = False

            # Check the line against all the polygons
            for p in polys:

                # if the polygon intersects the line, break the loop
                if L.intersection(p):
                    intersects = True
                    break

            # If intersection has been found, continue with the next possible
            # division
            if intersects:
                continue

            # Local flag
            local_possible = True

            # Now we need to check if there are the same amount of ingredients
            # of each type at each side of the line

            # Check every kind of ingredient (per side)
            for ing_type in ingredients:

                # Get the set
                ing_set = ingredients[ing_type]

                # Get the centers of the ingredients
                ing_centers = [x[0] for x in ing_set]

                # Counter
                p = 0

                # For each center, if it's at the left of the line, add 1. If
                # it's at the right, sub 1
                for ing in ing_centers:
                    p += 1 if getSide(P1, P2, ing) else -1

                # It should be 0 if there are the same number of ingredients at each side
                if p != 0:
                    local_possible = False
                    break

            # If the current line is a possible line
            if local_possible:
                if draw:
                    ax.plot([P1[0], P2[0]], [P1[1], P2[1]])

                # Break the loop
                possible = True
                break
                    
        # If there are no possible divisions
        if not possible:
            print "Case #%i: FALSE" % (case + 1)
            continue
        else:
            print "Case #%i: TRUE" % (case + 1)

        if draw:
            ax.set_aspect(1)
            pyplot.show()

if __name__ == '__main__':
    main()
