import re
'''
Created on 13.5.2015
A program which asks the user to enter some text and then goes through the text 
and prepares a set of words, which appear in the given text.
@author: e1201757
'''

print(set([word for word in re.compile("\W").split(input("Please input some test:")) if word !='']))
