#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 30 11:28:07 2017

@author: ameetrawtani

Fast Fibonacci example with memoization
"""

def fastFib(n, memo = {0:1, 1:1}):
    '''Assumes n is an int >= 0, calls memo recursively.
    Returns Fibonacci of n
    
    Decided to initialize dictionary with base case.
    '''
    #base fibonacci
    #if n==0 or n==1:
    #    return 1
    try:
        return memo[n]
    except KeyError:
        result = fastFib(n-1, memo) + fastFib(n-2, memo)
        memo[n] = result
        return result