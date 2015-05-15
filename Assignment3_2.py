'''
Created on 15.5.2015

    A program, which finds and displays the total price of all products from the following text. 
    The price for each product is calculated by multiplying the amount of the product by its unit
     price:   name=Milk;amount=200;unit_price=0.9\nname=Bread;amount=134;unit_price=3.48\nname=Butter;
     amount=58;unit_price=1.65\nname=Cheese;amount=260;unit_price=4.35

@author: e1201757
'''
from itertools import product
def Text2List(priceText):
    productsList = []
    products = priceText.split('\n')
    for product in products:
        items = product.split(';')
        productDict = {}
        for item in items:
            productDict[(item.split('=')[0]).strip()] = (item.split('=')[1]).strip()
        productsList.append(productDict)
        
    return productsList

def calcTotalPrice(productsList):
    totalPrice = 0
    for product in productsList:
        amount = eval(product['amount'])
        unit_price = eval(product['unit_price'])
        totalPrice += amount * unit_price
    return totalPrice

priceText = 'name=Milk;amount=200;unit_price=0.9\nname=Bread;amount=134;unit_price=3.48\nname=Butter;amount=58;unit_price=1.65\nname=Cheese;amount=260;unit_price=4.35'
productsList = Text2List(priceText)
print('All products in a list:')
print(productsList)
print('The total price is:' + str(calcTotalPrice(productsList)))
    
    
            
