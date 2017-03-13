''' A program to have fun with the turtle.
Fall 2014
Lab 03
@authors Ethan Clark and Jacob Schott (elc3 and jps29)
'''

#Gain access to the collection of code named "turtle"
import turtle

#Give the name "window" to the screen where the turtle will appear
window = turtle.Screen()

#Create a turtle and name it bob
bob = turtle.Turtle()

#Import math.
import math

bob.hideturtle()
bob.penup()

#Ask user for x, y, x1, and y1 values.
x = int(input('please give the first value of x :'))
y = int(input('please give the first value of y :'))
x1 = int(input('please give the second value of x :'))
y1 = int(input('please give the second value of y :'))

#Make tuples of the user given points.
point1 = (x,y)
point2 = (x1,y1)

#Make bob go to the first tuple point.
bob.goto(point1)
bob.pendown()
bob.pensize(5)
bob.write(point1, font = ('Arial', 20, 'italic'))

#Make bob go to the second tuple point.
bob.goto(point2)
bob.write(point2, font = ('Arial', 20, 'italic'))
bob.penup()

#Make bob go below the line to write the caption.
list_y = [y, y1]
y2 = min(list_y)
list_x = [x, x1]
x2 = min(list_x)
bob.goto(x2, y2 - 50)

#Calculate the length of the line
x_line = x1 - x
y_line = y1 - y
hyp_line = math.sqrt(y_line**2 + x_line**2)
hyp_line = str(hyp_line)

#Have bob write the caption below the line
bob.write('This is the line you described!', font = ('Arial', 20, 'italic'))
bob.goto(x2, y2-80)
bob.write('Its length is ' + hyp_line, font = ('Arial', 20, 'italic'))

window.exitonclick()