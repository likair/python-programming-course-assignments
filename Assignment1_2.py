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

def a(i):
    if i == 1:
        return 1
    elif i == 2:
        return 1
    else:
        return a(i - 2) + a(i - 1)
    
def b(i):
    if i == 1:
        return 1
    elif i == 2:
        return 1
    elif i == 3:
        return 2
    else:
        return b(i - 3) + b(i - 2) + b(i - 1)
    
for i in range(1, 10):
    print(a(i), end=" ")
print()
for i in range(1, 10):
    print(b(i), end=" ")
    
