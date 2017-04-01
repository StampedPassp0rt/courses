#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  1 14:38:56 2017

@author: ameetrawtani
"""

from ps1_partition import get_partitions
import time

#================================
# Part A: Transporting Space Cows
#================================

def load_cows(filename):
    """
    Read the contents of the given file.  Assumes the file contents contain
    data in the form of comma-separated cow name, weight pairs, and return a
    dictionary containing cow names as keys and corresponding weights as values.

    Parameters:
    filename - the name of the data file as a string

    Returns:
    a dictionary of cow name (string), weight (int) pairs
    """

    cow_dict = dict()

    f = open(filename, 'r')

    for line in f:
        line_data = line.split(',')
        cow_dict[line_data[0]] = int(line_data[1])
    return cow_dict


# Problem 1

def greedy_cow_transport(cows,limit=10):
    cows = sorted(((v, k) for k, v in cows.items() if v <= limit))
    fit_no_more = limit - cows[0][0]
    train = []
    while cows:
        car_weight = 0
        car, over = [], []
        while car_weight <= fit_no_more and cows:
            car_weight, old = car_weight + cows[-1][0], car_weight
            if car_weight <= limit:
                car.append(cows.pop()[1])
            else:
                car_weight = old
                over.insert(0, cows.pop())
        train.append(car)
        cows += over
    return train

'''Testing portion'''
cows = load_cows("pset1/ps1_cow_data.txt")
limit=100
print(cows)




#print(brute_force_cow_transport(cows, limit))
