'''
Model a single particle
Created Fall 2014
Lab12
@author: Serita Nelesen (smn4) and Ethan Clark (elc3)
'''

#Import the math module for the collision testing in the Particle class.
import math
from helpers import *

#Set a constant variable for the dampening_factor.
DAMPENING_FACTOR = 0.88

#Create a class to model a particle.
class Particle:
    '''
    Particle models a single particle that may be rendered to a canvas.
        x and y will be within the dimensions of the canvas (0 to 400).
        velX and velY will be between -25 and 25.
        Radius is always 15.
        Color is generated randomly.
    '''
    
    #Constructor for the Particle class.
    def __init__(self, x = 50, y = 50, velX = 10, velY = 15, radius = 15, color = '#663977'):
        '''
        Constructor to receive the x, y, velocity x, velocity y, radius, and color
        of a particle and create the instance variables accordingly.
        '''
        
        #Set all the instance variables to the given (or default) values.
        self._x = x
        self._y = y
        self._velX = velX
        self._velY = velY
        self._radius = radius
        self._color = color
    
    #Method to put the particle (circle) on the canvas.    
    def render(self, canvas):
        '''
        Method that receives a canvas and creates an circle/particle on the canvas.
        '''
        canvas.create_oval(self._x - self._radius, self._y - self._radius, self._x + self._radius, 
                           self._y + self._radius, fill = self._color)
     
    #Method to move the particle on the canvas.    
    def move(self, canvas):
        '''
        Method to receive a canvas and moves the particle accordingly.
        '''
        
        #Check to see if the particle is at the left or right edge of the canvas.
        if self._x + self._radius > canvas.winfo_reqwidth() or self._x - self._radius < 0:
            self._velX = -1 * (self._velX)
            
        #Check to see if the particle is at the top or bottom of the canvas.
        if self._y + self._radius > canvas.winfo_reqheight() or self._y - self._radius < 0:
            self._velY = -1 * (self._velY)
            
        #Move the particle a certain number of pixels to the left, right, up, or down.
        self._x += self._velX
        self._y += self._velY
    
    #Accessor to access the x value of the particular particle.    
    def get_x(self):
        return self._x
    
    #Accessor to access the y value of the particular particle.
    def get_y(self):
        return self._y
    
    #Accessor to access the radius of the particular particle.
    def get_radius(self):
        return self._radius
    
    #Method to determine if two particles overlap or hit each other.
    def hits(self, other):
        '''
        Method that receives the instance self and another instance and determines
        if the two instances/particles overlap.
        '''
        
        if (self == other):
            # I can't collide with myself.
            return False
        else:
            # Determine if I overlap with the target particle.
            return (self._radius + other.get_radius()) >= distance(self._x, self._y, other.get_x(), other.get_y())
        
    #Method to determine how the particle bounces off of another particle.
    def bounce(self, target):
        
        ''' This method modifies this Particle object's velocities based on its
        collision with the given target particle. It modifies both the magnitude
        and the direction of the velocities based on the interacting magnitude
        and direction of particles. It only changes the velocities of this
        object; an additional call to bounce() on the other particle is required
        to implement a complete bounce interaction.
  
        The collision algorithm is based on a similar algorithm published by K.
        Terzidis, Algorithms for Visual Design.
  
        target  the other particle
         '''
        
        #Uses the hits method and if true, it will calculate how the particle bounces off.
        if self.hits(target):
            angle = math.atan2(target.get_y() - self._y, target.get_x() - self._x)
            targetX = self._x + math.cos(angle) * (self._radius + target.get_radius())
            targetY = self._y + math.sin(angle) * (self._radius + target.get_radius())
            ax = targetX - target.get_x()
            ay = targetY - target.get_y()
            self._velX = (self._velX - ax) * DAMPENING_FACTOR
            self._velY = (self._velY - ay) * DAMPENING_FACTOR
