#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 14 20:35:37 2017

@author: ameetrawtani

retirement plotting example
"""

import pylab as plt

#function to calculate compound interest
def retire(monthly, rate, terms):
    #initialize within the function
    savings = [0]
    base = [0]
    mRate = rate/12
    for i in range(terms):
        #label for x axis
        base += [i]
        #compounding savings and the monthly contribution.
        savings += [savings[-1]*(1+mRate) + monthly]
    #return the lists, base as x, savings as y.
    return base, savings


def displayRetireWMonthlies(monthlies, rates, terms):
    plt.figure('retireMonth')
    plt.clf()
    plt.xlim(30*12, 40*12)
    monthLabels = ['r', 'b', 'g', 'k']
    rateLabels = ['-', 'o', '--']
    for i in range(len(monthlies)):
        monthly = monthlies[i]
        monthLabel = monthLabels[i%len(monthLabels)]
        for j in range(len(rates)):
            rate = rates[j]
            rateLabel = rateLabels[j%len(rateLabels)]
            xvals, yvals = retire(monthly, rate, terms)
            plt.plot(xvals, yvals, monthLabel + rateLabel, label = 'retire:'+str(monthly) + ':' + str(int(rate*100)) + '%')
            plt.legend(loc = 'upper left')

    
#displayRetireWMonthlies([500, 600, 700, 800, 900, 1000, 1100], [0.05], 40*12)

#What if I get 12% annualized, and do this...
displayRetireWMonthlies([500, 700, 900, 1100], [0.09, 0.11, 0.13], 40*12)