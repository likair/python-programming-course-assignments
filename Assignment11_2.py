'''
Created on Jun 8, 2015

    A GUI application, which provides appropriate interface for entering the address of an 
    image on Internet and then download and save it to the local machine and display it on 
    the application.

@author: lebs
'''

from tkinter import messagebox, Entry, Label, Button, LEFT, END, Tk
from urllib import request
from os.path import basename,abspath

def download():
    global urlEntry
    url = urlEntry.get()
    urlEntry.delete(0, END)
    try:
        response = request.urlopen(url).read()
        fileName = basename(url)
        file = open(fileName,'wb')
        file.write(response)
        file.close()
        messagebox.showinfo(title="Congratulations", message='The picture "' + fileName + '" has been downloaded to: "' + abspath(fileName) + '".')
    except Exception as e:
        messagebox.showinfo(title="Error", message=str(e))


root = Tk()
root.wm_title('Picture Download')
root.geometry('300x50')
Label(root, text='Address: ').pack(side=LEFT)
urlEntry = Entry(root)
urlEntry.pack(side=LEFT)
Button(root, text='Download', command=download).pack(side=LEFT)




root.mainloop()