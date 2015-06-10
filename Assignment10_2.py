'''
Created on Jun 5, 2015
    
    A GUI application , which changes the background color of the main window as the 
    mouse moves above it.
    
@author: lebs
'''
from tkinter import *

def changeColor(Event):
    root.configure(background='black')

if __name__ == '__main__':
    root = Tk()
    root.wm_title('Color Change')
    root.geometry('500x500')
    root.bind('<Motion>',changeColor)
    root.mainloop()