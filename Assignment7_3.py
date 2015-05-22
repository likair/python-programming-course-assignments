'''
Created on 22.5.2015
    
    A program, which uses recursion to find all indexes of a substring (substr) in a string (str).

@author: e1201757
'''

def findAllIndexes(string, substring, index=0):
    if index > len(string) - len(substring) + 1:
        return ''
    else:
        index = string.find(substring, index)
        if index != -1:
            return str(index) + ', ' + findAllIndexes(string, substring, index + len(substring))    
        else: return ''
        
def findAllIndexes2(string, substring, index=0):
    return '' if index > len(string) - len(substring) + 1 else (str(index) + ', ' + findAllIndexes2(string, substring, index + len(substring))) if  substring == string[index: index + len(substring)] else findAllIndexes2(string, substring, index + 1)

print(findAllIndexes('1234521233412', '12')[:-2])

print(findAllIndexes2('1234521233412', '12')[:-2])

