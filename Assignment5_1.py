'''
Created on 19.5.2015

    A program which allows the user to write and read product data from a file. 
    The program should ask the user to enter product data (name, unit price and amount) 
    and write the data of each product to a separate line so that details are separated 
    By semicolon(;). For the search part the application should ask the user to enter the 
    criteria (name, unit price or amount) and search the product with the criteria equal 
    to the given value.
    
@author: e1201757
'''
FILEPATH = 'product_db.txt'

def writeToFile(content, filePath):
    file = open(filePath, 'a+')
    file.write(content + '\n')
    file.close()

def readFromFile(filePath):
    file = open(filePath, 'r')
    content = file.read().split('\n')
    content.pop()
    productsList = []
    for product in content:
        productDict = {}
        details = product.split(';')
        productDict['name'] = details[0]
        productDict['unit_price'] = details[1]
        productDict['amount'] = details[2]
        productsList.append(productDict)
    return productsList
        
def inputProductsFromConsole():
    text = ''
    while True:
        text = input('Please enter product data (name, unit price and amount), and use \';\' to separate(enter \'q\' to quit):')
        if text != 'q':
            writeToFile(text, FILEPATH)
        else: break
    
def searchProducts(criteria, value):
    productsList = readFromFile(FILEPATH)
    print('Search Result(s):')
    for productDict in productsList:
        if productDict[criteria] == value:
            print(productDict)

if __name__ == '__main__':
    inputProductsFromConsole()
    criteria = input('Enter the criteria to search:')
    value = input('Enter the value:')
    searchProducts(criteria, value)
    
    
    
    
    
    
