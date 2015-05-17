'''
Created on 15.5.2015

    A program in which you define a function for encrypting texts so that it receives a 
    text and converts 'flower' to 'garlic' and prints out the resulting text.

@author: e1201757
'''

print(input('Input some texts, then I will encrypt for you: ').translate(str.maketrans('flower', 'garlic')))
