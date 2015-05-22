'''
Created on 22.5.2015
    
    A program which uses lambda operator and map() function to convert each value x 
    in this list: [25,39,52,68,20,89] to a new value y according to these conditions:
     if x<50, y=0 if 50<x<=75, y=2, if x>=75, y=3.

@author: e1201757
'''
l = [25,39,52,68,20,89]
print(list(map(lambda x: 0 if x < 50 else 2 if x > 50 and x<=75 else 3 if x>=75 else None , l)))