# -*- coding: utf-8 -*-
"""
Created on Mon Nov 03 23:08:08 2014
@author: christianhamelain
"""

import random



class fireball :
    """Implements a fireball !
    value / status
    0 : not burned already
    1 : burning
    2 : burned
    """

    def __init__(self, size, violence, startingPoints) :
        """ Constructor of the class
        size : couple of int (size of the map)
        violence : int (probability of burning a neighboor point)
        startingPoints : List of couple of int (seats of fire)
        forest : List of List of couple of int (map)
        """

        # self.forest = [[0]*size[0]]*size[1]
        self.size = size
        self.forest = [[]]
        (x, y) = size
        for i in range(0, x) :
            """self.forest.append([])"""
            for j in range (0, y) :
                self.forest[i].append(0)
            # end for
            if (i < x ) :
                self.forest.append([])
        # end for
        
        """self.forest = [ [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]"""
                        
        self.startingPoints = startingPoints
        for point in startingPoints :
            (x, y) = point
            self.forest[x][y] = 1
        # end for
        self.fireZone = startingPoints
        self.violence = violence

        random.seed()
    # end of __init__ method

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
    # end of canBurn method

    def isBurned(self, point) :
        """couple of int -> bool
        return true if "point" is in the forest, and already burned
        """
        b = True
        (x, y) = point
        (c, d) = self.size
        """
        b = b and (x >= 0) and (x < len(self.forest[0]))
        b = b and (y >= 0) and (y < len(self.forest))
        """
        b = b and (x >= 0) and (x < c)
        b = b and (y >= 0) and (y < d)
        
        b = b and (self.forest[x][y] == 2)
        return b
    # end of isBurned method

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
                # end if
            # end for
            oldFirePoints.append(burningPoint)
        # end for
        for point in oldFirePoints :
            (x, y) = point
            self.fireZone.remove(point)
            self.forest[x][y] = 2
        for point in newFirePoints :
            (x, y) = point
            self.fireZone.append(point)
            self.forest[x][y] = 1
        # end for
    # end of nextState

    def isFinished(self) :
        """void -> bool
        returns true if there is no more fire
        """
        return (self.fireZone == [])
    # end of isFinished

    def displayForest(self) :
        """void -> void
        displays the forest
        """
        for i in self.forest :
            s = ""
            for j in i :
                a = str(j)
                if (j == 2) :
                    a = " "
                s = s + a + " "
            # end for
            print s
        # end for
    # end of displayForest

    def getForest(self) :
        """void -> List of list of couple of int
        returns the forest
        """
        return self.forest
    # end of getForest

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
            # end for
        # end for

        return vect
    #end of getCloseBurnedNeighboorsInForest
                        

    def enlargeYourPenis(self, length)  :
        """int -> void
        modifies the forest and enlarge each obstacles of "length"
        """
        newForest = [[]]
        (x, y) = self.size
        for i in range(0, x) :
            for j in range (0, y) :
                newForest[i].append(0)
            # end for
            if (i < x ) :
                newForest.append([])
        # end for

        for i in range(0, x) :
            for j in range(0, y) :
                newForest[i][j] = self.forest[i][j]
            # end for
        # end for
        
        for i in range(0, x) :
            for j in range(0, y) :
                if (self.forest[i][j] == 0) :
                    
                    vect = self.getCloseBurnedNeighboorsInForest(newForest, (i, j), length)
                    for point in vect :
                        (a, b) = point
                        newForest[a][b] = 0
                    # end for
                # end if
            # end for
        # end for
        self.forest = newForest
    # end of enlargeYourPenis

        
        

# end of fireball

test = fireball((10, 10), 490, [(5, 5)])

# test.nextState()
#test.displayForest()
print " "
"""
while (not test.isFinished()) :
    test.nextState()
    test.displayForest()
    print " "
"""


size = (100, 100)
number = random.randint(5, 10)

startVect = []

for i in range(1, number) :
    
    point = (random.randint(0, 99), random.randint(0, 99))
    if ( not (point in startVect)) :
        startVect.append(point)

superTest = fireball(size, 520, startVect)

while (not superTest.isFinished()) :
    superTest.nextState()
    

superTest.displayForest()

superTest.enlargeYourPenis(3)

superTest.displayForest()


