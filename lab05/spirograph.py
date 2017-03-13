''' A program to generate pictures like made from a spirograph.
Fall 2014
lab 05
@author Ethan Clark (elc3)
'''

#import the turtle and library libraries.
import turtle
import math

#Give the name "window" to the screen where the turtle will appear
window = turtle.Screen()

#Create a turtle and name it Ethan.
Ethan = turtle.Turtle()

while True:
    #Prompt the user if he or she wants to draw a spirograph.
    choice = input('Would you like to draw a spirograph? (Y/n):')
    if choice == 'n' or choice == 'N':
            break
    elif choice != 'Y' or choice != 'y':
            print("Please enter Y or n")
    else:
        #Prompt the user for the needed information.
        mov_rad = float(input("Please give the radius of the moving circle:"))
        fix_rad = float(input("Please give the radius of the fixed circle:"))
        pen_offset = float(input("Please give the offset of the pen point in the moving circle:"))
        color = input("Please give the desired color:")

        current_time = (0.0)
        x = (fix_rad + mov_rad) * math.cos(0) + pen_offset*math.cos((fix_rad + mov_rad)*(0 / mov_rad))
        y = (fix_rad + mov_rad) * math.sin(0) + pen_offset*math.sin((fix_rad + mov_rad)*(0 / mov_rad))
        Ethan.penup()
        Ethan.goto(x,y)
        Ethan.pendown()
        Ethan.color(color)

        while current_time < 100:
            current_time = current_time + 0.1
            x = (fix_rad + mov_rad) * math.cos(current_time) + pen_offset*math.cos((fix_rad + mov_rad)*(current_time / mov_rad))
            y = (fix_rad + mov_rad) * math.sin(current_time) + pen_offset*math.sin((fix_rad + mov_rad)*(current_time / mov_rad))
            Ethan.goto(x,y)

window.exitonclick()