'''
Created on 15.5.2015

    A program, which finds all the indexes of word 'flower' in the following text: 
    "A flower is a beautiful plant, which can be planted in the garden or used to decorate
     home. One might like a flower for its colors and the other might like a flower for its
    smell. A flower typically symbolizes soft feelings".

@author: e1201757
'''
test =  'A flower is a beautiful plant, which can be planted in the garden or used to decoratehome. One might like a flower for its colors and the other might like a flower for its smell. A flower typically symbolizes soft feelings'
index = 0

while index < len(test):
    index = test.find('flower', index)
    if index == -1:
        break
    print(index)
    index += 6

    