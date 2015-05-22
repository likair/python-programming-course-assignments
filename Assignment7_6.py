'''
Created on 22.5.2015
    
    A program, which uses reduce() function to calculate the greatest value in this list:  [25,39,52,68,20,89].

@author: e1201757
'''
import functools
l = [25, 39, 52, 68, 20, 89]
print(functools.reduce(lambda x, y: x if x > y else y, l))
