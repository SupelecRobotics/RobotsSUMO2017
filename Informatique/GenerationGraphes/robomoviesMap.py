# -*- coding: utf-8 -*-
"""
Created on Mon Nov 03 23:08:08 2014
@author: christianhamelain
"""

from incendieCopie import fireball 


size = (200, 300)

robomoviesForest = fireball(size, 0, (0, 0), (0, 0), (0, 0))

robomoviesForest.summonEfreet()

robomoviesForest.popCircle((20, 9), 3)

robomoviesForest.popCircle((175, 9), 3)

robomoviesForest.popCircle((185, 9), 3)

robomoviesForest.popCircle((10, 85), 3)

robomoviesForest.popCircle((20, 85), 3)

robomoviesForest.popCircle((135, 87), 4)

robomoviesForest.popCircle((177, 110), 3)

robomoviesForest.popCircle((140, 130), 3)

robomoviesForest.popCircle((140, 170), 3)

robomoviesForest.popCircle((177, 190), 3)

robomoviesForest.popCircle((135, 213), 4)

robomoviesForest.popCircle((10, 215), 3)

robomoviesForest.popCircle((20, 215), 3)

robomoviesForest.popCircle((20, 291), 3)

robomoviesForest.popCircle((175, 291), 3)

robomoviesForest.popCircle((185, 291), 3)



robomoviesForest.popCircle((175, 25), 5)

robomoviesForest.popCircle((83, 91), 5)

robomoviesForest.popCircle((165, 150), 5)

robomoviesForest.popCircle((83, 209), 5)

robomoviesForest.popCircle((175, 275), 5)



robomoviesForest.popRectangle((78, 0), (80, 40))

robomoviesForest.popRectangle((120, 0), (122, 40))

robomoviesForest.popRectangle((80, 0), (120, 7))

robomoviesForest.popRectangle((0, 26), (7, 34))

robomoviesForest.popRectangle((0, 56), (7, 64))

robomoviesForest.popRectangle((0, 236), (7, 244))

robomoviesForest.popRectangle((0, 266), (7, 274))

robomoviesForest.popRectangle((0, 96), (59, 204))

robomoviesForest.popRectangle((190, 120), (200, 180))

robomoviesForest.popRectangle((78, 260), (80, 300))

robomoviesForest.popRectangle((120, 260), (122, 300))

robomoviesForest.popRectangle((80, 293), (120, 300))

"""robomoviesForest.unZoom(2)"""

robomoviesForest.enclose()

robomoviesForest.displayForest()

