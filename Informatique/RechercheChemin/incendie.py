# -*- coding: utf-8 -*-
"""
Created on Mon Nov 03 23:08:08 2014
@author: christianhamelain
"""

import random

import math

from carte import Map

class Fireball(Map) :
    """Implements a Fireball !
    value / status
    0 : not burned already
    1 : burning
    2 : burned
    """

    def __init__(self, size, violence, rangeNumber, rangeX, rangeY) :
        """Constructor of the class
        size : couple of int (size of the map)
        forest : matrix of couple of int (the map)
        violence : int (probability of burning a neighboor point)
        rangeNumber : couple of int (range of the number of fire seats)
        rangeX : couple of int (range of x coordinates of fire seats)
        rangeY : couple of int (range of y coordinates of fire seats)
        startingPoints : list of couple of int (first fire seats)
        fireZone : list of couple of int (contains coordinates of each burning point)
        """
        
        random.seed()
        
        (x1, y1) = rangeNumber
        number = random.randint(x1, y1)

        (x2, y2) = rangeX
        (x3, y3) = rangeY

        startingPoints = []

        for i in range(1, number) :
    
            point = (random.randint(x2, y2), random.randint(x3, y3))
            if ( not (point in startingPoints)) :
                startingPoints.append(point)

        self.size = size
        self.forest = [[]]
        (x, y) = size
        for i in range(0, x) :
            
            for j in range (0, y) :
                self.forest[i].append(0)
            if (i < x ) :
                self.forest.append([])
        
        self.startingPoints = startingPoints
        
        for point in startingPoints :
            (x, y) = point
            self.forest[x][y] = 1

        self.fireZone = startingPoints
        self.violence = violence
    # end of __init__

    def empireStrikesBack(self, startingPoints) :
        """list of couple of int -> void
        delete previously set fire seats and set "startingPoints" as new fire seats
        """
        for point in self.startingPoints :
            (x, y) = point
            self.forest[x][y] = 0

        self.startingPoints = startingPoints
        
        for point in startingPoints :
            (x, y) = point
            self.forest[x][y] = 1

        self.fireZone = startingPoints
    # end of empireStrikesBack

    def canBurn(self, point) :
        """couple of int -> bool
        return true if "point" is in the forest, and not already burned
        """
        b = True
        (x, y) = point
        (c, d) = self.size
        b = b and (x >= 0) and (x < c)
        b = b and (y >= 0) and (y < d)
        b = b and (self.forest[x][y] == 0)
        return b
    # end of canBurn

    def isBurned(self, point) :
        """couple of int -> bool
        return true if "point" is in the forest, and already burned
        """
        b = True
        (x, y) = point
        (c, d) = self.size

        b = b and (x >= 0) and (x < c)
        b = b and (y >= 0) and (y < d)
        
        b = b and (self.forest[x][y] == 2)
        return b
    # end of isBurned
    
    def getBurnedNeighboors(self, center) :
        """couple of int -> List of couple of int
        returns the List of neighboors of center that are already burned
        """
        vectlist = []
        (x, y) = center
        temp = [x - 1, y]
        if self.isBurned(temp) :
            vectlist.append(temp)
        temp = [x + 1, y]
        if self.isBurned(temp) :
            vectlist.append(temp)
        temp = [x, y - 1]
        if self.isBurned(temp) :
            vectlist.append(temp)
        temp = [x, y + 1]
        if self.isBurned(temp) :
            vectlist.append(temp)
        return vectlist
    # end of getBurnedNeighboors
    
    def getBurnableNeighboors(self, center) :
        """couple of int -> List of couple of int
        returns the List of neighboors of center that can burn
        """
        vectlist = []
        (x, y) = center
        temp = [x - 1, y]
        if self.canBurn(temp) :
            vectlist.append(temp)
        temp = [x + 1, y]
        if self.canBurn(temp) :
            vectlist.append(temp)
        temp = [x, y - 1]
        if self.canBurn(temp) :
            vectlist.append(temp)
        temp = [x, y + 1]
        if self.canBurn(temp) :
            vectlist.append(temp)
        return vectlist
    # end of getBurnableNeighboors
    
    def nextState(self) :
        """void -> void
        this does the propagation of the fire in the forest after one step
        """
        newFirePoints = []
        oldFirePoints = []
        for burningPoint in self.fireZone :
            for point in self.getBurnableNeighboors(burningPoint) :
                if (random.randint(1, 1000) <= self.violence) :
                    newFirePoints.append(point)

            oldFirePoints.append(burningPoint)
 
        for point in oldFirePoints :
            (x, y) = point
            self.fireZone.remove(point)
            self.forest[x][y] = 2
        for point in newFirePoints :
            (x, y) = point
            self.fireZone.append(point)
            self.forest[x][y] = 1
    # end of nextState

    def isFinished(self) :
        """void -> bool
        returns true if there is no more fire
        """
        return (self.fireZone == [])
    # end of isFinished



    def getCloseBurnedNeighboorsInForest(self, forest, center, length) :
        """List of list of couple of int, couple of int, int -> list of list of couple of int
        returns the burned points closer than "length" of the center
        """
        vect = []
        (x, y) = center
        for i in range(x - length, x + length) :
            a = length - abs(i - x)
            for j in range(y - a, y + a) :
                    
                b = True
                (c, d) = self.size
                b = b and (i >= 0) and (i < c)
                b = b and (j >= 0) and (j < d)
        
                b = b and (forest[i][j] == 2)

                if b :
                    vect.append((i, j))
                    
        return vect
    #end of getCloseBurnedNeighboorsInForest
                        
    
##    def enlargeYourPenis2(self, length, obstacleRate)  :
##        """int, int -> void
##        modifies the forest and enlarge each obstacles of "length"
##        """
##        newForest = [[]]
##        (x, y) = self.size
##        for i in range(0, x) :
##            for j in range (0, y) :
##                newForest[i].append(0)
##
##            if (i < x ) :
##                newForest.append([])
##
##        for i in range(0, x) :
##            for j in range(0, y) :
##                newForest[i][j] = self.forest[i][j]
##        
##        for i in range(0, x) :
##            for j in range(0, y) :
##                if (self.forest[i][j] <= 0 and self.forest[i][j] >= obstacleRate) :
##                    
##                    vect = self.getCloseBurnedNeighboorsInForest(newForest, (i, j), length)
##                    for point in vect :
##                        (a, b) = point
##                        newForest[a][b] = 0
##        self.forest = newForest
##    # end of enlargeYourPenis2
##    """


    def allumerLeFeu(self) :
        """void -> void
        burn the forest to the end
        """
        while (not self.isFinished()) :
            self.nextState()
    # end of allumerLeFeu

    def readyToUse(self, length, obstacleRate) :
        """int, int -> void
        run the fire and enclose the map with obstacles at "obstacleRate"
        """
        self.allumerLeFeu()
        self.enlargeYourPenis(length, obstacleRate)
        self.enclose(0)
    # end of readyToUse

    def summonEfreet(self) :
        """void -> void
        burn the whole forest
        """
        newForest = [[]]
        (x, y) = self.size
        for i in range(0, x) :
            for j in range (0, y) :
                newForest[i].append(2)

            if (i < x ) :
                newForest.append([])
        self.forest = newForest
    # end of summonEfreet



                  
                    
# end of Fireball



"""print " "


size = (100, 100)

superTest = Fireball(size, 520, (5, 10), (0, 99), (0, 99))

#superTest.empireStrikesBack([(1, 1)])

superTest.readyToUse(3, 0)

superTest.summonEfreet()

superTest.popCircle((10, 10), 4, -1)

superTest.displayForest()"""



