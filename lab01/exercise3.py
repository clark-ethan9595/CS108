''' A turtle program to draw a CS
Created Fall 2014
Lab 01
@author Ethan Clark (elc3)
'''

#Gain access to the collection of code named "turtle"
import turtle

#Give the name "window" to the screen where the turtle will appear
window = turtle.Screen()

#Create a turtle and name it bob
bob = turtle.Turtle()

#Tell bob to make a letter C
bob.backward(100)
bob.right(90)
bob.forward(200)
bob.left(90)
bob.forward(100)

#Tell bob to pick up the pen
bob.penup()

#Tell bob to turn left 90 degrees
bob.left(90)

#Tell bob to move forward 200 pixels
bob.forward(200)

#Tell bob to turn right 90 degrees
bob.right(90)

#Tell bob to move forward 150 pixels
bob.forward(150)

#Tell bob to put pen down
bob.pendown()

#Tell bob to make the letter S
bob.left(180)
bob.forward(100)
bob.left(90)
bob.forward(100)
bob.left(90)
bob.forward(100)
bob.right(90)
bob.forward(100)
bob.right(90)
bob.forward(100)

#Keep the window open until it is clicked
window.exitonclick() 