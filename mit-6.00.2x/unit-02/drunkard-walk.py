#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 16 18:12:10 2017

@author: ameetrawtani

Unit 2, Lecture 6: Random walk with location and drunk example
"""
import pylab as plt

#Location class.

class Location(object):
    def __init__(self, x, y):
        """x and y are floats that describe the Cartesian, 2-D location"""
        #allowing for inheritance
        self.x = x
        self.y = y
        
    #The function for moving...    
    def move(self, deltaX, deltaY):
        """deltaX and deltaY are floats for change in position."""
        #calls Location and reinitializes with old coordinates plus the delta
        return Location(self.x + deltaX, self.y + deltaY)
        
    def getX(self):
        return self.x
    
    def getY(self):
        return self.y
        
    def distFrom(self, other):
        #other is a location object with coordinates x and y. 
        #Want to know distance from it.
        ox = other.x
        oy = other.y
        xDist = self.x - ox
        yDist = self.y - oy
        return ((xDist**2+yDist**2)**(0.5))
        
    #string for current location
    def __str__(self):
        return '<' + str(self.x) + ', '\
            +str(self.y) + '>'

class Field(object):
    #making the location of the drunk an attribute of field rather than the drunk.
    def __init__(self):
        #field in this case is a mapping of drunk to location, so an empty dict.
        #b/c drunk will be in dictionary, the drunk key has to be hashable.
        #Unbounded field with as many entries for drunks as you want..
        self.drunks = {}

    def addDrunk(self, drunk, loc):
        #error handling: make sure not adding duplicate people
        if drunk in self.drunks:
            raise ValueError('Duplicate drunk')
        else:
            self.drunks[drunk] = loc
    
    def getLoc(self, drunk):
        if drunk not in self.drunks:
            raise ValueError('Drunk not in field')
        else:
            return self.drunks[drunk]

    def moveDrunk(self, drunk):
        #defensive programming - can't move what's not in the dict.
        if drunk not in self.drunks:
            raise ValueError('Drunk not in field')
        xDist, yDist = drunk.takeStep() # method from drunk class
        currentLocation = self.drunks[drunk]
        #use move method of Location to get new Location
        #the value in the dict for drunks is a location object.
        self.drunks[drunk] = currentLocation.move(xDist, yDist)
        
class Drunk(object):
    #This is a base class, meant to be inherited...
    # for example, will use it to create two sub-classes.
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'This drunk is named ' + self.name
        
    
"""Two drunk sub-classes: usual, and the move south one."""

import random

#instead of object, use Drunk as the actual object so it also takes info from base..
class UsualDrunk(Drunk):
    def takeStep(self):
        stepChoices = [(0.0, 1.0), (0.0, -1.0), (1.0, 0.0), (-1.0, 0.0)]
        return random.choice(stepChoices)
        
class ColdDrunk(Drunk):
    def takeStep(self):
        #arbitrary choice of making the North movement 0.9 instead of 1.0.
        #could as easily have been 0.5
        stepChoices = [(0.0, 0.9), (0.0, -1.1), (-1.0, 0.0), (1.0, 0.0)]
        return random.choice(stepChoices)
        
#function to simulate one walk.
def walk(f, d, numSteps):
    """Assumes: f is a Field, d is a Drunk in f, and numSteps is an int >= 0.
    Moves d numSteps times; returns the distance between the final location and 
    origin."""
    start = f.getLoc(d)
    for s in range(numSteps):
        f.moveDrunk(d)
    #references the Location object for starting location, and asks for distance
    #from it to the final location for drunk d in field f. Which can get with
    # f.getloc(d) after steps done.
    return start.distFrom(f.getLoc(d))
    
#simulate multiple walks....
def simWalks(numSteps, numTrials, dClass):
    """Assumes numSteps is an int >=0, numTrials an int > 0, dClass a subclass
    of Drunk.
    Simulates numTrials walks of numSteps steps each.
    Returns a list of final distances for each trial."""
    Homer = dClass("")
    origin = Location(0, 0)
    distances = []
    for t in range(numTrials):
        f = Field()
        f.addDrunk(Homer, origin)
        distances.append(round(walk(f, Homer, numSteps), 1))
    return distances
    

def drunkTest(walkLengths, numTrials, dClass):
    """Assumes walkLengths a sequence of ints>=0,
    numTrials  an int > 0,
    dClass a subclass of Drunk.
    For each number of steps in walkLengths, runs simWalks with numTrials walks
    and prints results"""
    
    for numSteps in walkLengths:
        distances = simWalks(numSteps, numTrials, dClass)
        
        print(dClass.__name__, 'random walk of ', numSteps, 'steps')
        print (' Mean = ', round(sum(distances)/len(distances), 4))
        print (' Max = ', max(distances), ' Min = ', min(distances))
    
#random.seed(0)
#drunkTest([10, 100, 1000, 10000], 100, UsualDrunk)
#



random.seed(0)
simAll((UsualDrunk, ColdDrunk), (1,10,100,1000,10000), 100)

"""Some plotting"""

#rotate through a sequence of styles defined by init.
class styleIterator(object):
    def __init__(self, styles):
        self.index = 0
        self.styles = styles
        
    def nextStyle(self):
        result = self.styles[self.index]
        if self.index == len(self.styles) - 1:
            self.index = 0
        else:
            self.index += 1
        return result
        
def simDrunk(numTrials, dClass, walkLengths):
    meanDistances = []
    for numSteps in walkLengths:
        print ("starting simulation of ", numSteps, ' steps')
        trials = simWalks(numSteps, numTrials, dClass)
        mean = sum(trials)/len(trials)
        meanDistances.append(mean)
    return meanDistances
    
def simAll(drunkKinds, walkLengths, numTrials):
    styleChoice = styleIterator(('m-', 'b--', 'g-.'))
    plt.figure('simulation')
    plt.clf()
    for dClass in drunkKinds:
        curStyle = styleChoice.nextStyle()
        print ("Starting simulation of ", dClass.__name__)
        means = simDrunk(numTrials, dClass, walkLengths)
        plt.plot(walkLengths, means, curStyle, label = dClass.__name__)
    plt.title('Mean Distance from Origin (' + str(numTrials) + ' trials)')
    plt.xlabel('Number of Steps')
    plt.ylabel('Distance from Origin')
    plt.legend(loc = 'best')
    
numSteps = (10, 100, 1000, 10000)
simAll((UsualDrunk, ColdDrunk), numSteps, 100)

#Finding out where walk ends.

        
        
            