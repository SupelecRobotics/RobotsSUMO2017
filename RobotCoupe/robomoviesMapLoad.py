# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 22:46:04 2015

@author: Fabien
"""
from carte import Map

size = (201, 301)

robomoviesForest = Map(size)

robomoviesForest.loadTextFile('/home/pi/RobotsSUMO2017/RobotCoupe/mapZoneDepartElargie.txt')
