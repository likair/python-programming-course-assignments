'''
Created on May 17, 2015

    A program which draws a human face with eyebrows, eyes, nose and mouth.

@author: Likai
'''

import turtle
window = turtle.Screen()
brad = turtle.Turtle()
brad.shape('turtle')
brad.speed(10)
brad.penup()

def drawEye(brad, x=0, y=0):
    brad.goto(x, y)
    brad.pendown()
    brad.setheading(135)
    brad.circle(150, 90)
    brad.penup()
    brad.setheading(90)
    brad.goto(x - 55, y -30)
    brad.pendown()
    brad.circle(50)
    brad.penup()
    brad.goto(x - 105, y -30)
    brad.pendown()
    brad.dot(10)
    brad.penup()

def drawNose(brad, x=0, y=0):
    brad.goto(x, y)
    brad.pendown()
    brad.setheading(120)
    brad.forward(120)
    brad.left(120)
    brad.forward(120)
    brad.left(120)
    brad.forward(120)
    brad.penup()

def drawMouth(brad, x=0, y=0):
    brad.goto(x, y)
    brad.pendown()
    brad.setheading(-90)
    brad.circle(100, 180)
    brad.penup()

def drawHead(brad, x=0, y=0):
    brad.goto(x, y)
    brad.pendown()
    brad.circle(300)
    brad.penup()

drawEye(brad, -45, 120)
drawEye(brad, 250, 120)
drawNose(brad, 60, -60)
drawMouth(brad, -100, -120)
drawHead(brad, 300, 0)

window.exitonclick()


