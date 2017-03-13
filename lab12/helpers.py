'''
Helper functions for lab 12
Created Fall 2014
Lab12
@author: smn4
'''
from random import randint

# Return a random color string in the form #RRGGBB
def getRandomColor():
    color = "#"
    for j in range(6):
        color += toHexChar(randint(0, 15)) # Add a random digit
    return color

# Convert an integer to a single hex digit in a character 
def toHexChar(hexValue):
    if 0 <= hexValue <= 9:
        return chr(hexValue + ord('0'))
    else:  # 10 <= hexValue <= 15
        return chr(hexValue - 10 + ord('A'))

# Distance between two points
def distance(x, y, x1, y1):
    return ((x - x1) ** 2 + (y - y1) ** 2)**0.5