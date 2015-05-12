'''
Created on May 12, 2015

@author: Likai
'''
'''
A program which prints out values belonging to the  following series:  
1 1 2 3 5 8 13 21 ...
1 1 2 4 7 13 24 44 ...
1 3 4 6 14 9 37 12 ...
'''
MAX = 10;  

def a(x):
    if x == 0:
        return 1
    elif x == 1:
        return 1
    else:
        return a(x - 2) + a(x - 1)
    
def b(x):
    if x == 0:
        return 1
    elif x == 1:
        return 1
    elif x == 2:
        return 2
    else:
        return b(x - 3) + b(x - 2) + b(x - 1)
    
def c(x):
    numbers = [0] * MAX
    numbers[0], numbers[1] = 1, 3
    i, j, k = 2, 0, 0
    for i in range(2, MAX):
        if i % 2 == 0:
            for j in range(i):
                numbers[i] += numbers[j]
        else:
            k += 1
            numbers[i] = (i - k) * numbers[1]
    return numbers[x]

def c2(x):
    if x == 0: return 1
    elif x == 1: return 3
    elif x % 2: return int((x + 1) / 2 * 3)
    else:
        s = 0
        for i in range(x):
            s += c2(i)
        return s
    
print('the question 1 ')
for i in range(MAX):
    print(a(i), end=" ")
print()
print()
print('the question 2 ')
for i in range(MAX):
    print(b(i), end=" ")
print()
print()
print('the question 3 ')
for i in range(MAX):
    print(c(i), end=" ")
print()
print()
print('the question 3 (different way) ')
for i in range(MAX):
    print(c2(i), end=" ")
                   


