'''
Created on 12.5.2015

@author: e1201757
'''
MAX = 10
a = [0] * MAX
a[1],a[2], a[3] = 1, 2, 5
for i in range(4, MAX):
    a[i] = a[i-3] + a[i-2] +a[i-1]/2
for i in range(1, MAX):
    print("a[" + str(i) + "] = " + str(a[i]))