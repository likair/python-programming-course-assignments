'''
Created on 22.5.2015
    
    A program, which uses recursion to calculate the sum of values between n and m, 
    where n and m can be any integer number.

@author: e1201757
'''
def sumCalc(n, m):
    if n == m:
        return 0
    else:
        return n + sumCalc(n + 1, m)
    
print(sumCalc(1, 101))