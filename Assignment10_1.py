'''
Created on Jun 5, 2015

    A GUI application, which displays a window for reading the width and height of 
    a shape and then draws it. The shape can be either a rectangle or an oval and 
    it should also be read from an Entry widget.

@author: lebs
'''
from tkinter import *

def drawRectangle():
    global shapeEntry, canvas
    canvas.pack_forget()
    shape = shapeEntry.get()
    width = shape.split(',')[0]
    height = shape.split(',')[1]
    canvas=Canvas(root, height=300, width=400)
    canvas.create_rectangle(10,10,eval(width),eval(height))
    canvas.pack()
    
def drawOval():
    global shapeEntry, canvas
    canvas.pack_forget()
    shape = shapeEntry.get()
    width = shape.split(',')[0]
    height = shape.split(',')[1]
    canvas=Canvas(root, height=300, width=400)
    canvas.create_oval(10,10,eval(width),eval(height))
    canvas.pack()

if __name__ == '__main__':
    root = Tk()
    root.wm_title('Draw')
    root.geometry('400x400+50+60')
    root.resizable(width=True, height=False)
    label=Label(root, text='Enter width,height:')
    label.pack()
    shapeEntry=Entry(root)
    shapeEntry.pack()
    canvas=Canvas(root, height=300, width=400)
    button1=Button(root, text='Rectangle', command=drawRectangle)
    button2=Button(root, text='oval', command=drawOval)
    button1.pack()
    button2.pack()
    
    root.mainloop()