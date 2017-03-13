'''
Model a planet
Created Fall 2014
Lab10
@author: smn4, elc3
'''

import turtle

class Planet:
    '''
    A class to model a planet.
    Invariants:
        Mass must be greater than zero.
        Distance from the sun must be greater than zero.
        Radius must be greater than zero.
    '''
    
    def __init__(self, name, rad, m, dist, color):
        
        if rad <= 0:
            raise ValueError('Planet radius must be positive!')
        else:
            self._radius = rad
                
        if m <= 0:
            raise ValueError('Planet mass must be positive!')
        else:
            self._mass = m
                
        if dist <= 0:
            raise ValueError("Planet distance from sun must be positive!")
        else:
            self._distance = dist
            
        self._x = dist
        self._y = 0    
        self._name = name
        self._color = color
            
        self._turtle = turtle.Turtle()
        self._turtle.penup()
        self._turtle.color(self._color)
        self._turtle.shape('circle')
        self._turtle.shapesize(self._radius, self._radius)
        self._turtle.goto(self._x, self._y)
        
    def get_name(self):
        return self._name
    
    def get_radius(self):
        return self._radius
    
    def get_mass(self):
        return self._mass
    
    def get_distance(self):
        return self._distance
    
    def set_name(self, newname):
        self._name = newname
    
    def __str__(self):
        return self._name
    
#--------------MAINCODE--------------
if __name__ == "__main__":
    try:
        p1 = Planet('Mars', 10, 500, 20, 'red')
        p2 = Planet('Jupiter', 10, 50, 30, 'orange')
    except ValueError as ve:
        print(ve)
    try:
        p3 = Planet('Mercury', -10, 50, 80, 'pink')
    except ValueError as ve:
        print(ve)
    try:
        p4 = Planet('Saturn', 10, -50, 75, 'yellow')
    except ValueError as ve:
        print(ve)
    try:
        p5 = Planet('Neptune', 10, 50, -60, 'blue')
    except ValueError as ve:
        print(ve)