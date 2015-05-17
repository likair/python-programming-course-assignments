'''
Created on May 17, 2015

    A program which asks the user to enter a command like f for fire and q for quit 
    and if the user enter f it shoots a ball and shows how it drops down gradually.

@author: Likai
'''
import turtle

trigger = input('Input \'f\' for fire and \'q\' for quit:')
V0 = 50

if trigger == 'f':
    print('Boom!')
    window = turtle.Screen()
    brad = turtle.Turtle()
    brad.shape('circle')
    brad.dot(20, 'red')
    for t in range(10):
        x = V0 * t
        y = -0.5 * 10 * t **2
        brad.goto(x, y)
        brad.dot(1)
    window.exitonclick()
    
elif trigger == 'q':
    print('The program has been terminated!')