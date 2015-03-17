# -*- coding: utf-8 -*-
"""
Created on Mon Nov 03 23:08:08 2014
@author: christianhamelain
"""
from carte import Map


size = (41, 61)

robomoviesForest = Map(size)




robomoviesForest.enclose(0)


# départ 1

robomoviesForest.popRectangle((16,0),(16,8),0)

robomoviesForest.popRectangle((24,0),(24,8),0)

robomoviesForest.popRectangle((16,0),(24,1),0)

# popcorn

robomoviesForest.popRectangle((0,5),(2,7),0)

robomoviesForest.popRectangle((0,11),(2,13),0)

robomoviesForest.popRectangle((0,47),(2,49),0)

robomoviesForest.popRectangle((0,53),(2,55),0)

# marches

robomoviesForest.popRectangle((0,19),(12,41),0)

# estrade

robomoviesForest.popRectangle((38,24),(40,36),0)

# départ 2

robomoviesForest.popRectangle((16,52),(16,60),0)

robomoviesForest.popRectangle((24,52),(24,60),0)

robomoviesForest.popRectangle((16,59),(24,60),0)


robomoviesForest.enlargeYourPenis(3, -1)


#robomoviesForest.displayForest()


