# -*- coding: utf-8 -*-
"""
Created on Mon Dec 15 23:08:08 2014
@author: christianhamelain
"""

import random

import math

class Map   :
    """Implements a Map !
    """
    def __init__(self, size)  :
        """Constructor of the class
        size : couple of int (size of the map)
        forest : matrix of couple of int (the map)
        """
        self.size = size

        self.forest = [[]]
        (x, y) = size
        for i in range(0, x) :
            
            for j in range (0, y) :
                self.forest[i].append(1)
            if (i < x ) :
                self.forest.append([])

        
        
    def isInTheForest(self, point)  :
        """couple of int -> bool
        return true if "point" is in the forest
        """
        b = True
        (x, y) = point
        (c, d) = self.size

        b = b and (x >= 0) and (x < c)
        b = b and (y >= 0) and (y < d)
        
        return b
    # end of isInTheForest

    def displayForest(self) :
        """void -> void
        displays the forest
        """
        for i in self.forest :
            s = ""
            for j in i :
                a = str(j)
                if (j > 0) :
                    a = " "
                else    :
                    a = str( (-j)%10)
                s = s + a + " "

            print s
    # end of displayForest


    def getForest(self) :
        """void -> List of list of couple of int
        returns the forest
        """
        return self.forest
    # end of getForest


    def enclose(self, obstacleLevel)   :
        """int -> void
        set obstacles on the merge of the forest, which level is "obstacleLevel"
        """
            
        (x, y) = self.size
        for j in range(0, y) :
            self.forest[0][j] = obstacleLevel
            self.forest[x - 1][j] = obstacleLevel
        
        for i in range(1, x - 1) :
            self.forest[i][0] = obstacleLevel
            self.forest[i][y - 1] = obstacleLevel
    # end of enclose

    def popRectangle(self, point1, point2, obstacleLevel)  :
        """couple of int, couple of int, int -> void
        set obstacles, which level is "obstacleLevel", in the rectangle delimited by "point1" and "point2"
        """
        (x1, y1) = point1
        (x2, y2) = point2

        minx = min(x1, x2)
        maxx = max(x1, x2)
        miny = min(y1, y2)
        maxy = max(y1, y2)

        for x in range(minx, maxx + 1)  :
            for y in range(miny, maxy + 1)  :
                if(self.isInTheForest((x,y))) :
                    self.forest[x][y] = obstacleLevel
    # end of popRectangle
    
    def popCircle(self, center, radius, obstacleLevel) :
        """couple of int, int, int -> void
        set obstacles, which level is "obstacleLevel", in the disc defined by "center" and "radius"
        """
        (x, y) = center

        for i in range(x - radius - 1, x + radius + 1) :
            for j in range(y - radius - 1, y + radius + 1)  :
                if(self.isInTheForest((i, j)) and ( math.sqrt((i - x)*(i - x) + (j - y)*(j - y)) <= radius)) :
                    self.forest[i][j] = obstacleLevel
    # end of popCircle

    def unZoom(self, factor)    :
        """int -> void
        replaces the forest by a forest "factor" times less big, and change obstacles in the same way
        """
        (l, w) = self.size
        newLength = l / factor + 1
        newWidth = w / factor + 1
        newForest = [[]]
        for i in range(0, newLength) :
            for j in range (0, newWidth) :
                newForest[i].append(1)

            if (i < newLength ) :
                newForest.append([])

        
        for x in range(0, newLength )    :
            for y in range(0, newWidth ) :
                b = 1
                for i in range(x * factor, (x + 1) * factor + 1)    :
                    for j in range(y * factor, (y + 1) * factor + 1)    :
                        if(self.isInTheForest((i, j)))    :

                            if(self.forest[i][j] <= 0)    :
                                if(b <= 0) :
                                    b = max(b, self.forest[i][j])
                                else    :
                                    b = self.forest[i][j]
                
                newForest[x][y] = b

        self.size = (newLength, newWidth)

        self.forest = newForest
    # end of unZoom

    def getCloseFreeNeighboorsInForest(self, forest, center, length) :
        """List of list of couple of int, couple of int, int -> list of list of couple of int
        returns the burned points closer than "length" of the center
        """
        vect = []
        (x, y) = center
        for i in range(x - length, x + length + 1) :
            a = length - abs(i - x)
            for j in range(y - a, y + a + 1) :
                    
                b = True
                (c, d) = self.size
                b = b and (i >= 0) and (i < c)
                b = b and (j >= 0) and (j < d)
        
                b = b and (forest[i][j] > 0)

                if b :
                    vect.append((i, j))
                    
        return vect
    #end of getCloseBurnedNeighboorsInForest

    def enlargeYourPenis(self, length, obstacleRate)  :
        """int, int -> void
        modifies the forest and enlarge each obstacles, which levels are higher than
        "obstacleRate", of "length"
        """
        newForest = [[]]
        (x, y) = self.size
        for i in range(0, x) :
            for j in range (0, y) :
                newForest[i].append(0)

            if (i < x ) :
                newForest.append([])

        for i in range(0, x) :
            for j in range(0, y) :
                newForest[i][j] = self.forest[i][j]
        
        for i in range(0, x) :
            for j in range(0, y) :
                if (self.forest[i][j] <= 0 and self.forest[i][j] >= obstacleRate) :
                    
                    vect = self.getCloseFreeNeighboorsInForest(newForest, (i, j), length)
                    for point in vect :
                        (a, b) = point
                        newForest[a][b] = self.forest[i][j] - 1
        self.forest = newForest
    # end of enlargeYourPenis

