#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 16 11:46:31 2017

@author: ameetrawtani
"""
import random
def genEven():
    '''
    Returns a random number x, where 0 <= x < 100
    Please generate a uniform distribution over the even 
    numbers between 0 and 100 (not including 100).
    '''
    # Your code here
    return random.randrange(0, 100, 2)
    
    
def deterministicNumber():
    '''
    Deterministically generates and returns an even number between 9 and 21
    '''
    # The more interesting answer. Seed is set so that when this function is 
    #called, it will always return the same number.
    random.seed(0)
    return 2 * random.randint(5,10)
    
    #Another option would have been to manually set one integer value between 10 and 20
    #inclusive for it to return, always, when called.
    
def stochasticNumber():
    '''
    Stochastically generates and returns a uniformly distributed even number between 9 and 21
    '''
    # Your code here - looks same in idea as genEven()
    return random.randrange(10, 21, 2)

'''These two dists are the same b/c random.random is a uniform distribution.
The offset of -1 changes it so that it ranges from [-1.0, 1.0) vs. [0.0, 1.0)'''
def dist1():
    return random.random() * 2 - 1

def dist2():
    if random.random() > 0.5:
        return random.random()
    else:
        return random.random() - 1 

'''Trying out a simulation for a boxcar - two sixes for a pair of die.'''

def rollDie():
    return random.randint(1,6)

def fracBoxCars(numTests):
    numBoxCars = 0
    for i in range(numTests):
        #each i is a trial
        if rollDie() == 6 and rollDie() == 6:
            numBoxCars += 1
    return numBoxCars/numTests
    
print ("Frequency of double sixes = " + str(fracBoxCars(100000)*100) + "%")