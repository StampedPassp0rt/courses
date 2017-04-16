#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 14 17:09:43 2017

@author: ameetrawtani
"""

import pylab as plt

mySamples = []
myLinear = []
myQuadratic = []
myCubic = []
myExponential = []

for i in range(0,30):
    mySamples.append(i)
    myLinear.append(i)
    myQuadratic.append(i**2)
    myCubic.append(i**3)
    myExponential.append(1.5**i)
    
#first trial - in script.
#format: plt.plot(x, y)
plt.plot(mySamples, myLinear)
plt.plot(mySamples, myQuadratic)
plt.plot(mySamples, myCubic)
plt.plot(mySamples, myExponential)

#second trial - if new, creates. If existing, opens the existing and adds/alters.
#in pylab, looks like the labels are associated with each figure assigned to.
#And assumed to be the one closest to and above it.
plt.figure('lin')
plt.xlabel('sample points')
plt.ylabel('linear function')
plt.plot(mySamples, myLinear)
plt.figure('quad')
plt.xlabel('sample points')
plt.ylabel('quadratic function')
plt.plot(mySamples, myQuadratic)
plt.figure('cubic')
plt.xlabel('sample points')
plt.plot(mySamples, myCubic)
plt.figure('expo')
plt.plot(mySamples, myExponential)
plt.xlabel('sample points')
plt.ylabel('exponential function')

plt.figure('cubic')
plt.ylabel('cubic function')

#titles
#plt.clf clears the window.
plt.figure('lin')
plt.clf()
plt.title('Linear')
plt.plot(mySamples, myLinear)

plt.figure('quad')
plt.clf()
plt.title('Quadratic')
plt.plot(mySamples, myQuadratic)
plt.figure('cubic')
plt.clf()
plt.title('Cubic')
plt.plot(mySamples, myCubic)
plt.figure('expo')
plt.clf()
plt.title('Exponential')
plt.plot(mySamples, myExponential)


#Visualizing differences

#Option 1: Manually set limits
plt.figure('lin')
plt.clf()
plt.title('Linear')
plt.ylim(0,1000)
plt.plot(mySamples, myLinear)

plt.figure('quad')
plt.clf()
plt.title('Quadratic')
plt.ylim(0, 1000)
plt.plot(mySamples, myQuadratic)

plt.figure('cubic')
plt.clf()
plt.title('Cubic')
plt.ylim(0,1000)
plt.plot(mySamples, myCubic)

plt.figure('expo')
plt.clf()
plt.title('Exponential')
plt.ylim(0, 1000)
plt.plot(mySamples, myExponential)


#Option 2: Plot multiple functions
#Just create a new figure, and call the plots in the same figure.
plt.figure('cubic expo')
plt.clf()
plt.title('Cubic vs Exponential')

plt.plot(mySamples, myCubic, 'g^', label = 'cubic', linewidth = 2.0)
plt.plot(mySamples, myExponential, 'r--',label = 'exponential', linewidth = 3.0)
#Legend has to be after the plots.
plt.legend(loc = 'upper left')

plt.figure('lin quad')
plt.clf()
#the terse part controls color and type of point.
plt.plot(mySamples, myLinear, 'b-', label = 'linear', linewidth = 4.0)
plt.plot(mySamples, myQuadratic, 'ro', label = 'quadratic', linewidth = 5.0)
plt.legend(loc = 'upper left')
plt.title('Linear vs Quadratic')

#subplots
#takes the # of rows, cols and which location to use.
plt.figure('cubic expo')
plt.clf()

plt.subplot(2,1,1)
plt.ylim(0, 140000)
plt.plot(mySamples, myCubic, 'b-', label = 'cubic')
plt.legend(loc = 'upper left')
plt.subplot(2,1,2)
plt.plot(mySamples, myExponential, 'g^', label = 'quadratic', linewidth = 3.0)
plt.ylim(0, 140000)
plt.legend(loc = 'upper left')
plt.title('Cubic vs Exponential')


#Changing the scale to logarithm.
plt.figure('quad cubic expo')
plt.yscale('log')
plt.plot(mySamples, myQuadratic,  label = 'quadratic')
plt.plot(mySamples, myCubic, label = 'cubic')
plt.plot(mySamples, myExponential, label = 'exponential')
plt.legend(loc = 'upper left')
plt.title('Non Linear Fxns')








