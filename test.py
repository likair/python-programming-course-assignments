'''
Created on 12.5.2015

@author: e1201757
'''
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
year = 2008
day = 28 if (year % 4) or ((year % 400) and not(year % 100)) else 29
print(day)




