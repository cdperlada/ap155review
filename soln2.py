# -*- coding: utf-8 -*-
"""
Created on Mon Aug 22 19:14:45 2016

@author: cdperlada
"""

import numpy as np
import random as random



#8.1a
dice1 = np.random.randint(1,6)
dice2 = np.random.randint(1,6)
if __name__ == "__main__":    
    print dice1
    print dice2
    
#8.1b
num = 1000000
    
doubles = 0
for k in range(num):
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    if dice1+dice2==12:
        doubles+=1
if __name__ == "__main__":    
    print float(doubles)/float(num)
    print 1/36.0
    