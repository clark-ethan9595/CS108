'''
Model a sun
Created Fall 2014
Lab10
@author: smn4, elc3
'''

import turtle

class Sun:
    '''
    A class to model the sun.
    Invariants:
        Radius must be greater than zero.
        Mass must be greater than zero.
        Temperature must be greater than absolute zero.
    '''

    def __init__(self, name, rad, m, temp):
        if rad <= 0:
            raise ValueError("The sun's radius must be positive!")
        else:
            self._radius = rad
                
        if m <= 0:
            raise ValueError("The sun's mass must be positive!")
        else:
            self._mass = m
                
        if temp <= -273.15:
            raise ValueError("The sun's temperature must be greater than absolute zero!")
        else:
            self._temp = temp
                
        self._name = name
        self._x = 0
        self._y = 0
            
        self._turtle = turtle.Turtle()
        self._turtle.shape('circle')
        self._turtle.color('yellow')
        self._turtle.goto(self._x, self._y)
            
    def get_mass(self):
        return self._mass
    
    def __str__(self):
        return self._name
    
#------------MAINCODE----------
if __name__ == "__main__":
    try:
        s1 = Sun('Sun', 10, 50, 5000)
        s2 = Sun('FireBall', 15, 5, -100)
    except ValueError as ve:
        print(ve)
    try:
        s3 = Sun('Glowing Sphere', -15, 10, -270)
    except ValueError as ve:
        print(ve)
    try:
        s4 = Sun('My Sun', 15, -10, 1000)
    except ValueError as ve:
        print(ve)
    try:
        s5 = Sun('THE Sun', 15, 10, -300)
    except ValueError as ve:
        print(ve)
        