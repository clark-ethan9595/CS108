''' Drawing Stick Figure
September 11, 2014
Lab 02
@author Serita Nelesen (smn4) 
@authors Ethan and Mollie (elc3 and mfh6)
'''

#Gain access to the collection of code named "turtle"
import turtle

#Give the name "window" to the screen where the turtle will appear
window = turtle.Screen()

#Create a turtle and name it bob
bob = turtle.Turtle()

#Gain access to the math library
import math

#Make UNIT equal to 50 pixels
UNIT = 50

#Make a refer to the Pythagorean theorem.
a = math.sqrt(pow(UNIT, 2) + pow(UNIT,2))

#Draw a stick figure guy
bob.pensize(3)
bob.forward(UNIT*2)
bob.penup()
bob.left(90)
bob.forward(UNIT*3)
bob.left(90)
bob.forward(UNIT)
bob.pendown()
bob.circle(UNIT)
bob.penup()
bob.left(90)
bob.forward(UNIT*2)
bob.pendown()
bob.forward(UNIT*2)
bob.right(45)
bob.forward(a)
bob.penup()
bob.left(135)
bob.forward(UNIT*2)
bob.pendown()
bob.left(135)
bob.forward(a)


#Keep the window open until it is clicked
window.exitonclick()