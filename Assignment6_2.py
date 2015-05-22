'''
Created on 20.5.2015

    A program, in you use regular expresions to split the following text and find and display the total
     price of all products from the following text. The price for each product is calculated by multiplying 
     the amount of the product by its unit price:   name=Milk;amount=200;unit_price=0.9\nname=Bread;amount=134;
     unit_price=3.48\nname=Butter;amount=58;unit_price=1.65\nname=Cheese;amount=260;unit_price=4.35
     
@author: e1201757
'''
import re

text = 'name=Milk;amount=200;unit_price=0.9\nname=Bread;amount=134;unit_price=3.48\nname=Butter;amount=58;unit_price=1.65\nname=Cheese;amount=260;unit_price=4.35'


def calcDigits(digits):
    s = 0
    for i in range(0, len(digits), 2):
        s += digits[i] * digits[i + 1]
    return s

# method 1: remove the other characters except digits
digits1 = [eval(digit) for digit in re.sub(r'[_a-zA-Z=\\\n]', '', text).split(';') if digit != '']
# method 1: find all digits
digits2 = [eval(digit) for digit in re.findall('\d+\.?\d*', text)]

print(calcDigits(digits1))
print(calcDigits(digits2))