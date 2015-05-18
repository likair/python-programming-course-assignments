import re
'''
Created on 13.5.2015

    A program which asks the user to enter some text and then goes through the text 
    and prepares a set of words, which appear in the given text.

@author: e1201757
'''
# we use nonword characters to split the string got from the user's input.
# we use set to remove the duplicate elements 
print(set([word for word in re.compile("[^a-zA-Z0-9\\-öäåÖÄÅ]+").split(input("Please input some test:")) if word !='']))