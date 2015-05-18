'''
Created on May 17, 2015

    A program, which draws a human face with falling tear drops.

@author: Likai
'''

import turtle
window = turtle.Screen()
brad = turtle.Turtle()
brad.shape('turtle')
brad.speed(100)
brad.penup()
def drawTears(brad, x=0, y=0, times=4):
    brad.speed(3)
    brad.setheading(-90)
    for i in range(times):
        brad.goto(x, y - i * 40)
        brad.pendown()
        brad.dot(20, 'blue')
        brad.penup()
        brad.goto(x-295, y - i * 40)
        brad.pendown()
        brad.dot(20, 'blue')
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
    brad.color('red')
    brad.begin_fill()
    brad.circle(50)
    brad.end_fill()
    brad.color('black')
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
drawTears(brad, 144, 14)

window.exitonclick()