'''
Created on 15.5.2015

    A program in which you define a function, which receives a list of values x0, x1, x2,...xn 
    and calculates the value of y in the following formula: y=∑sin2(xn) -log(xn,3)+1/pow(xn,5), 
    for n=0,1,2,...

@author: e1201757
'''
from math import sin, log

def calcFormula(valuesList):
    y = 0
    for xn in valuesList:
        if(isinstance(xn, int) or isinstance(xn, float) and not xn in (0, 1) ):
            y += sin(2*xn) - log(xn, 3) + 1/pow(xn, 5)
        else: return None
    return y
valuesList = ['a', 2, 3]
y = calcFormula(valuesList)
if y != None: print(calcFormula([2, 3, 4]))
else: print('Error input!')   
    
    
    
    