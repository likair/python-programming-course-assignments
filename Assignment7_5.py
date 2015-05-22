'''
Created on 22.5.2015
    
    A program which uses filter() to filter out values less than 50 in this list: [25,39,52,68,20,89].

@author: e1201757
'''
l = [25,39,52,68,20,89]
print(list(filter(lambda x: x < 50, l)))