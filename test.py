'''
Created on 12.5.2015

@author: e1201757
'''
from random import choice
'''
foo=0
print([x[:] for x in [[foo]*10]*10])

a = [[1, 2, 3], [4, 5 , 6], [7, 8, 9]]
c=[[0]*len(a)]*len(a[0])
print(c)
'''
'''
matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
#0
print(list(zip(*matrix)))
#1
print([[row[i] for row in matrix] for i in range(4)])
#2
transposed = []
for i in range(4):
    transposed.append([row[i] for row in matrix])
print(transposed)
#3
transposed = []
for i in range(4):
    # the following 3 lines implement the nested listcomp
    transposed_row = []
    for row in matrix:
        transposed_row.append(row[i])
    transposed.append(transposed_row)
print(transposed)
'''
'''
a = [1, 2, 3, 4, 5]
b = [1, 2, 3, 4, 5]

for i, j in zip(a, b):
    print(str(i) + ' ' + str(j))

print([(i, j) for i, j in zip(a, b)])
'''
'''
matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
print(*matrix)
print(list(zip(*matrix)))
'''
'''
a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
b = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
c = []
for i in range(0, len(a)):
    c.append([])
    for j in range(0, len(a[0])):
        c[i].append(a[i][j] + b[i][j])
print(c)
'''
'''
a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
b = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
#c = list([0] * len(a[0])) * len(a)
#c = [0] * len(a[0])
#c = [[0] * len(a[0])] * len(a)
#d = c * 3
#d = list(c) * 3
c = [[0]*3]*3
#print(c)
for i in range(len(c)):
    for j in range(len(c[0])):print(c[i][j], end=' ')
    print()
'''
'''
a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
b = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
c = [[0] * len(a)] * len(a[0]) # the mistake is here, because ... the copy lists will be changed as the first one
#c = [[0, 0, 0], [0, 0, 0], [0, 0, 0]] # This is the right way
#c = [i[:] for i in [[0] * len(a)] * len(a[0])] # This is the right way too
print('the initial state:')
print(c)
print()
time = 0
for i in range(len(a)):
    for j in range(len(a[0])):
        time +=1
        c[i][j] = a[i][j] + b[i][j]
        print('the ' + str(time) + ' time')
        print('c[' + str(i) + '][' + str(j) +'] = ' + str(c[i][j]))
        print(c)
        print()
print('the final result:')
print(c)
'''
'''
a = [[0] * 3] * 3
print(a)
a[0][0] = 1
print(a)
'''
'''
print([i[:] for i in [[0]*3]*3])
'''
'''
li = [1, '']
new_list = [ x for x in li if x != '' ]
print(new_list)
'''
'''
li = ['', '', '', 'a']
for s in li[:]:
    print(s)
    if s == '':
        li.remove(s)
print(li)
'''
'''
print("hello".maketrans('he', 'ab'))
'''
'''
a = ['x', 'x', 'x', '0']
b = []
for s in a:
    print(s)
    if s != 'x':
        #a.remove(s)
        b.append(s)
    a = b
    #print(a)   
print(a)
'''
'''
name = 'lebs'
age = 10
print(name, age)
print(name, age, sep=';')
'''
'''
day = 10
month = 3
year = 2015
print('{}/{}/{}'.format(day, month, year))
'''
'''
print('{}')
print('{}'.format('hello'))
'''
'''
# the default parameter sequence
print('{:5}{:8}'.format(456, 8973))
# 1 means the second parameter, 0 means the first parameter
print('{1:5}{0:8}'.format(456, 8973))
# It seems it will show all the length of parameter even we limit the length less than its length
print('{1:3}{0:5}'.format(456, 8973))
print('{:5.2}'.format(10/3))
'''
'''
import random
month = random.randrange(1, 13)
'''
'''
year = 2008
if (not year % 4 and year % 100) or not year % 400:
    print('leap')
'''
'''
a = (1, 2, 3, 4)
b = {}
for i in a: b[i] = 0
print(b)
'''
'''
print(int(1000/23))

num = 32
print(str(num)[1])
#print(len(num)) #wrong
print(len(str(num)))
'''
'''
# a method to replace the switch in other language
def f(x):
    return {
        'a': 1,
        'b': 2,
    }.get(x, 9)
'''
'''
import random
import time

def strTimeProp(start, end, format, prop):
    """Get a time at a proportion of a range of two formatted times.

    start and end should be strings specifying times formated in the
    given format (strftime-style), giving an interval [start, end].
    prop specifies how a proportion of the interval to be taken after
    start.  The returned time will be in the specified format.
    """

    stime = time.mktime(time.strptime(start, format))
    etime = time.mktime(time.strptime(end, format))

    ptime = stime + prop * (etime - stime)

    return time.strftime(format, time.localtime(ptime))


def randomDate(start, end, prop):
    return strTimeProp(start, end, '%m/%d/%Y %I:%M %p', prop)

print(randomDate("1/1/2008 1:30 PM", "1/1/2009 4:50 AM", random.random()))
'''
'''
import time
import datetime
#今天星期几
today=int(time.strftime("%w"))
print(today)
#某个日期星期几
anyday=datetime.datetime(2012, 4, 21).strftime("%w")
print(anyday)

'''
'''
sum = 0
for year in range(10):
    sum = (1000 + sum) * (1 + 0.047)
print(sum)
'''
'''
# get the current time
import time

print(time.strftime('%Y-%m-%d', time.localtime(time.time())))
'''
'''
# solve the equation
a = 10
b = 40
c = 15
delta =  ** 2 - 4 * a * c
if delta < 0:
    print(' No solution!')
elif delta == 0: 
    print('x = ' + str(-b / (2 * a)))
else: 
    print('x1 = ' + str((-b + delta ** 0.5) / (2 * a)))
    print('x2 = ' + str((-b - delta ** 0.5) / (2 * a)))
'''
'''
year = 2008
day = 28 if (year % 4) or ((year % 400) and not(year % 100)) else 29
print(day)
'''
#!/usr/bin/python
# -*- coding: utf-8 -*-
# Created on May 17, 2015
#    A program which generates randomly a number of date and time values and displays them in Finnish language.
# @author: Likai
'''

NUMBERS = ['nolla', 'yksi', 'kaksi', 'kolme', 'neljä', 'viisi', 'kuusi', 'seitsemän', 'kahdeksan', 'yhdeksän']
SUFFIX1 = ['', 'kymmentä', 'sata', 'tuhat']
SUFFIX2 = ['', 'kymmentä', 'sataa', 'tuhatta']

def numberInFinnish(num):
    if num < 10000:
        literality = ''
        i = 0
        if num == 0: return NUMBERS[0]
        while num > 0:
            digit = int(num % 10)
            num /= 10
            if digit == 1:
                if i == 1:
                    if literality == '':
                        literality = 'kymmenen'
                    else: literality += 'toista'
                else: literality = NUMBERS[digit] + SUFFIX1[i] + literality
            elif digit > 1:
                literality = NUMBERS[digit] + SUFFIX2[i] + literality
            i += 1
    else:
        literality = 'This number is not supported!'
    return literality

SUFFIX1 = ['', 'kymmentä ', 'sata ', 'tuhat ']
SUFFIX2 = ['', 'kymmentä ', 'sataa ', 'tuhatta ']

def numberInFinnish4(num):
    length = len(str(num))
    if length < 5:
        literality = ''
        for i in range(length):
            digit = length - i
            if  digit == 4:
                if str(num)[i] == '0': pass
                elif str(num)[i] == '1':
                    literality += NUMBERS[int(str(num)[i])] + 'tuhat '
                else: literality += NUMBERS[int(str(num)[i])] + 'tuhatta '
            elif digit == 3:
                if str(num)[i] == '0': pass
                elif str(num)[i] == '1':
                    literality += NUMBERS[int(str(num)[i])] + 'yksisata '
                else: literality += NUMBERS[int(str(num)[i])] + 'sattaa '
            elif digit == 2:
                if str(num)[i] == '0': pass
                elif str(num)[i] == '1':
                    if str(num)[i + 1] == '0':
                        literality += 'kymmenen'
                    else: literality += NUMBERS[int(str(num)[i + 1])] + 'toista'
                else: literality += NUMBERS[int(str(num)[i])] + 'kymmentä'
            elif digit == 1:
                if num == int(str(num)[i]) or (length > 1 and str(num)[i - 1] != '1' and str(num)[i] != '0'):
                    literality += NUMBERS[int(str(num)[i])]
        return literality
    else: return 'This number is not supported!'
  
for i in range(1001):
    print(numberInFinnish(i))

'''
'''
# format is very strong.
print('{1:6.3f}, {0:04d}'.format(1, 534.65464574))
'''
'''
import locale, time

locale.setlocale(locale.LC_ALL,'Finnish_Finland')
print(time.strftime('%H:%M %A, %d %B %Y', time.localtime()))
'''
'''
startTime = datetime.datetime(2015,5,1,8,15,30)

endTime = datetime.datetime(2015,5,15,12,15)

remainingTime = endTime-startTime

print ('Remaining time is ' + str(remainingTime))

#Here we define a date time format

dateTimeFormat='%d.%m.%Y %H:%M:%S'

#Here we define two date time strings

dateTimeString1='1.01.2015 20:30:15'

dateTimeString2='1.01.2015 20:31:00'

#Here we check whetehr the dateTimeString1 is a valid dateTime value, wchich

#matches the dateTimeFormat

dateTimeStruct1=time.strptime(dateTimeString1, dateTimeFormat)

#Here we check whetehr the dateTimeString2 is a valid dateTime value, wchich

#matches the dateTimeFormat

dateTimeStruct2=time.strptime(dateTimeString2, dateTimeFormat)

#here we make time ou tof the dateTimeStruct1

dateTime1=time.mktime(dateTimeStruct1)

#here we make time ou tof the dateTimeStruct1

dateTime2=time.mktime(dateTimeStruct2)

#Here we calculate the time difference between two dateTime values

timeDifference=(dateTime2 - dateTime1)

#Here we print the time difference between two dateTime values

print('The difefrence between ' + dateTimeString1 + ' and ' + dateTimeString2 + ' is ' +  str(timeDifference) + ' seconds')

'''
'''
import turtle

t=turtle.Turtle()

screen=turtle.Screen()

screen.tracer(8, 25)

dist = 5
for i in range(100):

    t.fd(dist)

    t.rt(45)

    dist += 5
'''
'''
def sum_(n):  
    return n + {True:lambda:sum_(n-1), False:lambda:0}[not not n]()  
print(sum_(100)
'''
# This is Example 5-1

# Here we define a function for reading the file
'''

def fileLength(filename):

    'returns the number of characters in file filename'
    
    infile = open(filename, 'r')
    
    content = infile.read()
    
    infile.close()
    
    return 'The number of characters in ' + filename + ' is ' + str(len(content))

# Here we define a function for reading the file

def fileContent(filename):

    'returns the content of file filename'
    
    infile = open(filename, 'r')
    
    content = infile.read()
    
    infile.close()
    
    return content

# Here we define a function for reading the file

def fileLines(filename):

    'returns the content of file filename'
    
    infile = open(filename, 'r')
    
    fileLines = infile.readlines()
    
    infile.close()
    
    return fileLines

# Here we define a function for reading the file

def fileLinesCount(filename):

    'returns the content of file filename'
    
    infile = open(filename, 'r')
    
    fileLines = infile.readlines()
    
    infile.close()
    
    return len(fileLines)

# Here we define a function for appending text to the file

def writeToFile(content, filename):

    'appends content to the filename'
    
    outfile = open(filename, 'a')
    
    outfile.write(content + '\n')
    
    outfile.close()
    
    return fileContent(filename);

 

# Here we ask the name of a file

filename = input('Enter file name: ')

content = input('Enter some text: ')

# Here we print the length of the file

print(writeToFile(content, filename))

print('Lines in the file:')

print(fileLines(filename))

print('Number of lines in the file:')

print(fileLinesCount(filename))
'''
'''
f = open('mysql.txt', 'r+')
f.readline()
f.close()
'''
'''
#Example 6-1
#Here we define the file path and name
file="C:/Temp/registry.txt"
try:
    #Here we open the file in read mode
    infile = open(file, "r")
    #Here we try to write to the file
    infile.write("Apple 100 1.99\nOrange 80 0.99\n")
    #infile.flush()
    infile.close()
#Here we catch the IO exception  
except IOError:
    print ('Error: can\'t find or write to ' + file + '!')
#Here we put the code in case there is no error  
else:
    print ('Data was written to the ' + file + ' successfully')
'''

# Here we define the file path and name
'''
file = "C:/Temp/registry.txt"
x = 2.56
y = 0
cont = 'yes'
try:
    s = cont + x  
    # Here we divide x by zero
    d = x / y
    # Here we open the file in read mode
    infile = open(file, "r")
    # Here we try to write to the file
    infile.write("Apple 100 1.99\nOrange 80 0.99\n")
    # infile.flush()
    infile.close()
# Here we catch TypeException
except TypeError:
    print ('Cannot sum text with number! ')
# Here we catch IOException  
except  IOError:
    print ('IOError! ')
# Here we catch ZeroDivisionError
except  ZeroDivisionError:
    print ('ZeroDivisionError')
# Here we put the code in case there is no error  
else:
    print ('The program was executed successfully')
'''
# Here we define the file path and name
'''
file="C:/Temp/registry.txt"
x=2.56
y=0
cont='yes'
try:
    s=cont + x  
    #Here we divide x by zero
    d=x/y
    #Here we open the file in read mode
    infile = open(file, "r")
    #Here we try to write to the file
    infile.write("Apple 100 1.99\nOrange 80 0.99\n")
    #infile.flush()
    infile.close()
#Here we catch TypeException
except:
    print ('There was an exception in the program!')
#Here we put the code in case there is no error  
else:
    print ('The program was executed successfully')
'''
'''
#Here we define the file path and name

file="C:/Temp/registry.txt"

x=2.56

y=0

cont='yes'

try:
    try:
        s=cont + x
    #Here we catch TypeException
    except TypeError as e:
        print ('Cannot sum text with number: ' + str(e))
    finally:
        print ('After trying to sum string with number')     
    #Here we divide x by zero
    d=x/y
    #Here we open the file in read mode
    infile = open(file, "r")
    #Here we try to write to the file
    infile.write("Apple 100 1.99\nOrange 80 0.99\n")
    #infile.flush()
    infile.close()
#Here we catch IOException  
except  IOError as e:
    print ('IOError: ' + str(e))
#Here we catch ZeroDivisionError
except  ZeroDivisionError as e:
    print ('ZeroDivisionError: ' + str(e))
#Here we put the code in case there is no error  
else:
    print ('The program was executed successfully')
finally:
    print ('The end of the program')
'''
'''
# We can also raise an exception manually. To do this we use raise command, like in the following:
y=0
try:
    if y==0:
        raise ArithmeticError
#Here we catch IOException  
except  ArithmeticError as e:
    print ('ArithmeticError ' + str(e) )
#Here we put the code in case there is no error  
else:
    print ('The program was executed successfully')
finally:
    print ('The end of the program')
'''
'''
print(zip([1, 2, 3], [1, 2, 3]))

def sum_1(n):  
    return n + {True:sum_1(n-1), False:0}[not not n]

def sum_2(n):
    return {n}
print(sum_2(2))
'''
'''
a = 1
def f():
    print(a)
def f2():
    global a
    a = 2
f()
f2()
print(a)
'''
'''
import re
if re.match('\d{3,5}', '12345'):
    print('M')
'''
'''
import re
text = '123445'
print(re.compile('1.*?5').findall(text))
'''
'''
import re
text = 'The sky may be sunny or cloudy, but still you should try to do your best to achieve your tiny joy.'
print(re.findall('.*y$', text))
'''
'''
import random

print(random.random())
print(random.randrange(10))
print(choice(range(1)))
'''
'''
print(choice(range(1)))
'''
'''
class Test:
    pass

dic = {}
dic[(Test())] = 1
print(dic)
'''
'''
locals()['player2'] = 1
print(locals()['player2'])
'''
'''
dic = {}
dic['test'] = 1
print(dic[0])   # wrong
'''  
'''
from tkinter import Tk, Button, RIDGE, BOTTOM,messagebox

from time import strftime, localtime

#Here we define a click handler function

def click_handler():

    'prints current day and time info'

    time=strftime('Day: %d %b %Y\nTime: %H:%M:%S %p\n', localtime())

    #Here we display the current date and time on a dialogbox

    messagebox.showinfo(title="Date & Time", message=time)

#Here we create the main window

root=Tk()

#Here we set the title of the window

root.wm_title("Main Window")

#Here we set the dimensions of the window

root.geometry('200x150')

#Here we set the position of the window

root.geometry('+150+200')

#Here we would set both the dimensions and position of the window

#root.geometry('200x200+50+60')

#Here is another way to specify the width and height of the window

#root.geometry('{}x{}'.format(150, 150))

#Here we make the window unresizable

root.resizable(width=False, height=False)

button=Button(root,

              text='Display Date & Time',

              command=click_handler)

button.pack(side=BOTTOM)

root.mainloop()
'''
from tkinter import Tk, Button, Label, Entry, END

from time import strptime, strftime, localtime

from tkinter.messagebox import showinfo

# Here we define a callback function for handling the event

def compute():

    'display day of the week corresponding to date in dateEnt; date must be in this format MMM DD, YYY'

    # Here we refer to the global variable dateEntry

    global dateEntry

    # Here we read date from entry dateEnt

    date = dateEntry.get()

    # Here we extract the weekday

    weekday = strftime('%A', strptime(date, '%b %d, %Y'))

   

    # Here we display the current date and time on a dialogbox

    showinfo(message='{} was a {}'.format(date, weekday))

    # Here we clear the current content of the entry

    dateEntry.delete(0, END)

# Here we create the main window

root = Tk()

# Here we set the title of the window

root.wm_title("Main Window")

# Here we set the dimensions of the window

root.geometry('200x100')

# Here we set the position of the window

root.geometry('+150+200')

# Here we would set both the dimensions and position of the window

# root.geometry('200x200+50+60')

# Here is another way to specify the width and height of the window

# root.geometry('{}x{}'.format(150, 150))

# Here we make the window unresizable
'''

root.resizable(width=True, height=False)

label = Label(root, text='Enter date')

label.grid(row=0, column=0)

# Here we add an Entry object

dateEntry = Entry(root)

dateEntry.grid(row=0, column=1)

# Here we add a Button object

button = Button(root,

              text='Enter',

              command=compute)

button.grid(row=2, column=1, columnspan=3)

root.mainloop()
'''
'''
from tkinter import Tk, Canvas, Frame, Button, SUNKEN, LEFT, RIGHT

#Here we define a callback function for handling the button clicking

def up():

    'initializes the start of te curve to mouse position'

    #Here we access the globa variables y and canvas

    global y, canvas

    canvas.create_line(x, y, x, y-20)

    y -=20

#Here we define a callback function for handling the button clicking

def down():

    'initializes the start of te curve to mouse position'

    #Here we access the globa variables y and canvas

    global y, canvas

    canvas.create_line(x, y, x, y+20)

    y +=20

  

#Here we define a callback function for handling the button clicking

def right():

    'initializes the start of te curve to mouse position'

    #Here we access the globa variables y and canvas

    global x, canvas

    canvas.create_line(x, y, x+20, y)

    x +=20

#Here we define a callback function for handling the button clicking

def left():

    'initializes the start of te curve to mouse position'

    #Here we access the globa variables y and canvas

    global x, canvas

    canvas.create_line(x, y, x-20, y)

    x -=20

  

#Here we create the main window

root=Tk()

root.geometry('400x300')

root.wm_title('Plotting Window')

#Here we define a Canvas object

canvas=Canvas(root, height=200, width=200, relief=SUNKEN, borderwidth=20)

canvas.pack(side=LEFT)

#Here we define a frame to hold four buttons

buttonFrame=Frame(root)

buttonFrame.pack(side=RIGHT)

#Here we specify the buttons

button=Button(buttonFrame, text='Up', command=up)

button.grid(row=0, column=0, columnspan=2)

button=Button(buttonFrame, text='Left', command=left)

button.grid(row=1, column=0)

button=Button(buttonFrame, text='Right', command=right)

button.grid(row=1, column=1)

button=Button(buttonFrame, text='Down', command=down)

button.grid(row=2, column=0, columnspan=2)

#Here we specify the initail pen position

x, y=120, 100

root.mainloop()
'''
import re
import os

text = 'https://portal.vamk.fi/pluginfile.php/1/theme_formal_white/customlogourl/1432199285/tunnus.png'
result = os.path.basename(text)
print(result)













