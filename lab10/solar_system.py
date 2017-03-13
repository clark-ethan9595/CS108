'''
Model of a solar system
Created Fall 2014

@author: smn4
'''

from sun import *
from planet import *

class Solar_System:
    
    def __init__(self):
        self._sun = None
        self._planets = []
        
    def add_sun(self, a_sun):
        if isinstance(a_sun, Sun):
            self._sun = a_sun
        else:
            raise TypeError('add_sun(): cannot add ' + str(type(a_sun)) + ' to solar system.')
            
    def add_planet(self, a_planet):
        if isinstance(a_planet, Planet):
            self._planet = a_planet
        else:
            raise TypeError('add_planet(): cannot add ' + str(type(a_planet)) + ' to solar system.')
            
    def show_planets(self):
        for a_planet in self._planets:
            print(a_planet)
            
#----------MAINCODE------------
if __name__ == "__main__":
    try:
        ss1 = Solar_System()
        ss1.add_sun(Sun('FireBall', 20, 1000, 5000))
        ss1.add_planet(Planet('Mars', 30, 40, 50, 'blue'))
    except TypeError as te:
        print(te)
    
    ss2 = Solar_System()
    
    try:
        ss2.add_sun("NOT A SUN")
    except TypeError as te:
        print(te)
        
    try:
        ss2.add_planet("NOT A PLANET")
    except TypeError as te:
        print(te)
        