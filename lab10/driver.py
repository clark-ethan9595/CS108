'''
Program to be the driver to create a visual representation of a solar system.
Created on Nov 6, 2014
Lab10
@author: elc3
'''

import turtle
from solar_system import *

window = turtle.Screen()
window.setworldcoordinates(-1, -1, 1, 1)

ss = Solar_System() 
ss.add_sun(Sun("SUN", 19.5, 1000, 5800))
ss.add_planet(Planet("EARTH", .475, 5000, 0.3, 'blue'))

try:
    new_planet = input('Please enter the name of the planet: ')
    new_radius = float(input('Please enter the radius of the planet (between 0 and 1): '))
    new_mass = float(input('Please enter the mass of the planet: '))
    new_dist = float(input('Please enter the distance of the planet from the sun (between 0 and 1): '))
    new_color = input('Please enter the color of the planet: ')
    ss.add_planet(Planet(new_planet, new_radius, new_mass, new_dist, new_color))
except ValueError:
    print('Invalid input for new planet!')

#Keep the window open until it is clicked
window.exitonclick()    