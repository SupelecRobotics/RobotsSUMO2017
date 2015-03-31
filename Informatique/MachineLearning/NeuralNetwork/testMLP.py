# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 15:21:31 2015

test MLP

@author: Darkpudding
"""

import numpy as np
import MLP

hiddenLayerSizes = np.array([200,50])
lienL = 'learningDict'
lienT = 'learningDict'
test = MLP.MLP(lienL, lienT, hiddenLayerSizes, fparam1=1, fparam2=1, epsilon=0.0001)

#test.learn()
#test.saveMLP()

test.loadMLP()
outputs = test.predict()
test.comparerTout(outputs)
test.comparer1(outputs,73)