'''
Created on Jun 5, 2015

    A GUI application, which consists of two buttons and the program should work so 
    that when the first button is clicked, the second button should disappear if it 
    is visible and vice versa. The application should also work so that if the mouse 
    is moved above the second button, the first button will be moved up.

@author: lebs
'''
from tkinter import *

def changeButton2(Event):
    global button2, visible
    if visible == 1:
        button2.grid_remove()
        visible = 0
    
    elif visible == 0:
        button2.grid()
        visible = 1
    

def changeButton1(Event):
    global button2, x
    x += 1
    button2.grid_remove()
    button2.grid(row = x, column = 1)

if __name__ == '__main__':
    root = Tk()
    button1 = Button(root, text='Click')
    button2 = Button(root, text='Move')
    button1.grid(row=0, column=0)
    visible = 1
    button2.grid(row=0, column=1)
    x = 0
    button1.bind('<Button-1>', changeButton2)
    button2.bind('<Motion>', changeButton1)
    root.mainloop()