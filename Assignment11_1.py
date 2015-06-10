'''
Created on Jun 8, 2015

    A GUI application which provides appropriate interfaces to enter and search product 
    information (id, name, amount and unit price) to and from a SQLITE3 database. 
    The application should allow searching product data based on name or unit price. 

@author: lebs
'''

from tkinter import messagebox, Entry, Button, Tk, Label
import sqlite3
from os.path import exists
from tkinter.constants import END

dbPath = 'pdt.db'
def search():
    global idEntry, nameEntry, amountEntry, unitPriceEntry
    productID = idEntry.get()
    name = nameEntry.get()
    amount = amountEntry.get()
    unitPrice = unitPriceEntry.get()
    con = sqlite3.connect(dbPath)
    cur = con.cursor()
    if productID == '' and name == '' and amount == '' and unitPrice == '':
        query = 'SELECT * FROM product'
    else:
        query = 'SELECT * FROM product WHERE '
        if productID != '':
            query += 'id = ' + productID + ' '
        if name != '':
            query += 'name = ' + name + ' '
        if amount != '':
            query += 'amount = ' + amount + ' '
        if unitPrice != '':
            query += 'unit_price = ' + unitPrice
    
    cur.execute(query)
    result = cur.fetchall()
    formatResult = ''
    for product in result:
        formatResult += 'id: ' + str(product[0]) + '\n'
        formatResult += 'name: ' + product[1] + '\n'
        formatResult += 'amount: ' + str(product[2]) + '\n'
        formatResult += 'unit price: ' + str(product[3]) + '\n'
        formatResult += '-------------------------------\n'
        
    messagebox.showinfo(title='Result', message=formatResult)
    con.close()
    idEntry.delete(0, END)
    nameEntry.delete(0, END)
    amountEntry.delete(0, END)
    unitPriceEntry.delete(0, END)
    
def create():
    global idEntry, nameEntry, amountEntry, unitPriceEntry
    productID = idEntry.get()
    name = nameEntry.get()
    amount = amountEntry.get()
    unitPrice = unitPriceEntry.get()
    con = sqlite3.connect(dbPath)
    cur = con.cursor()
    cur.execute("INSERT INTO product VALUES({}, '{}', {}, {})".format(productID, name, amount, unitPrice))
    con.commit()
    con.close()
    messagebox.showinfo(title='Congratulations', message='This product has been created successfully!')
    idEntry.delete(0, END)
    nameEntry.delete(0, END)
    amountEntry.delete(0, END)
    unitPriceEntry.delete(0, END)

if not exists(dbPath):
    con = sqlite3.connect(dbPath)
    cur = con.cursor()
    cur.execute('CREATE TABLE product(id int, name text, amount int, unit_price float)')
    con.commit()
    con.close()
root = Tk()
root.wm_title('Product Manager')

Label(root, text='id:').grid(row=0, column=0)
idEntry = Entry(root)
idEntry.grid(row=0, column=1)

Label(root, text='name:').grid(row=1, column=0)
nameEntry = Entry(root)
nameEntry.grid(row=1, column=1)

Label(root, text='amount:').grid(row=2, column=0)
amountEntry = Entry(root)
amountEntry.grid(row=2, column=1)

Label(root, text='unit price:').grid(row=3, column=0)
unitPriceEntry = Entry(root)
unitPriceEntry.grid(row=3, column=1)

Button(root, text='Search', command=search).grid(row=4, column=0)
Button(root, text='Create', command=create).grid(row=4, column=1)




root.mainloop()
