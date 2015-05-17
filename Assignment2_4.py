import re
'''
Created on 13.5.2015

    A program which asks the user to enter some text and then goes through the text 
    and puts each word and the number of its occurrence to a dictionary and then 
    prints out the content of the dictionary. 

@author: e1201757
'''
test = input("Please input some test:")
# remove the non word part
wordsList = re.compile("[^a-zA-Z0-9\\-öäå]+").split(test)
dic = {}
for word in wordsList:
        if not word in dic.keys():
            dic[word] = wordsList.count(word)

print(dic)
