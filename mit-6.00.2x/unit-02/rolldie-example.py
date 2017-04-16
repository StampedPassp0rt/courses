#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 16 11:37:31 2017

@author: ameetrawtani
"""

import random

def RollDie():
    return random.choice([1,2,3,4,5,6])
    
def testRoll(n=10):
    result = ''
    for i in range(n):
        result = result + 'Roll ' + str(i+1) + ': ' + str(RollDie()) + '\n'
    print (result)