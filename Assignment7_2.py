'''
Created on 22.5.2015
    
    A program which uses recursion to calculate the sum of n values of this series: 1/5, 1/17,...1/(3n+2).

@author: e1201757
'''
def calcSeries(n):
    if n == 1:
        return 1/5
    else:
        return 1/(3 * n + 2) + calcSeries(n - 1)

print(calcSeries(2))
