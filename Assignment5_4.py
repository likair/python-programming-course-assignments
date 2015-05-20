'''
Created on 19.5.2015

    Improve your program for problem 2 so that you catch possible exceptions and 
    print a user-friendly message both to the screen and to a log file.
    
@author: e1201757
'''

import os
import time

DB_PATH = 'product_db.txt'
LOG_PATH = 'log.txt'

def logError(errorMsg, filePath):
    try:
        file = open(filePath, 'a+')
        file.write(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())) + '\n' + errorMsg + '\n\n')
    except IOError as e:
        print('IOError: ' + str(e))
    finally:
        file.close()    
        
def writeToFile(content, filePath):
    try:
        file = open(filePath, 'a+')
        file.write(content + '\n')
    except IOError as e:
        logError(str(e), LOG_PATH)
        print('IOError: ' + str(e))
    finally:
        file.close()

def readFromFile(filePath):
    if os.path.exists(filePath):
        try:
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
        except IOError as e:
            logError(str(e), LOG_PATH)
            print('IOError: ' + str(e))
        finally:
            file.close()
    return []
        
def inputProductsFromConsole():
    text = ''
    while True:
        print('Please enter product data (name;unit price;amount), and use \';\' to separate(enter \'ENTER\' to quit).')
        print('For example: Apple;2;100')
        text = input('New product:').replace(' ', '')
        if text == '': 
            print('---------------------------------------')
            break        
        elif validateProduct(text):
            writeToFile(text, DB_PATH)
            print('New data have been saved.')
        input('Enter \'ENTER\' to continue.')
        print('---------------------------------------')

def validateProduct(text):
    details = text.split(';')
    try:    
        if len(details) != 3 or eval(details[1]) < 0 or eval(details[2]) < 0 :
            raise Exception
        return True
    except:
        errorMsg = 'Wrong data format.'
        logError(errorMsg, LOG_PATH)
        print(errorMsg)
    return False
    
def searchProducts(criteria, value):
    productsList = readFromFile(DB_PATH)
    correctProducts = []
    print('Search Result(s):')
    for productDict in productsList:
        if productDict[criteria] == value:
            correctProducts.append(productDict)
    if correctProducts != []:
        for productDict in correctProducts:
            printProduct(productDict)
    else: print('No Product has been found!\n')
    input('Enter \'ENTER\' to continue.')
    print('---------------------------------------')
        
def showAllProducts(filePath):
    productsList = readFromFile(filePath)
    if productsList != []:
        numOfProducts = 0;
        totolValues = 0;
        for productDict in productsList:
            totolValues += eval(productDict['unit_price']) * eval(productDict['amount'])
            numOfProducts += 1
            printProduct(productDict)
        print('* The number of products: ' + str(numOfProducts) + '.')
        print('* The sum of total values of each product:' + str(totolValues) + '.')
        print()
    else: print('No product has been found!\n')     
    input('Enter \'ENTER\' to continue.')  
    print('---------------------------------------') 
        
def printProduct(productDict):
    print('name: ' + productDict['name'])
    print('unit price: ' + productDict['unit_price'])
    print('amount: ' + productDict['amount'])
    print('* total value: ' + str(eval(productDict['unit_price']) * eval(productDict['amount'])))
    print('---------------------------------------')

if __name__ == '__main__':
    while True:
        print('******Products Information System******\n\n1. Enter new product data.\n2. Search by criteria in products database \n3. Show all products infomation.\n4. Quit.\n')
        choice = input('Please select:')
        print('---------------------------------------')
        if choice == '1':
            inputProductsFromConsole()
        elif choice == '2':
            criteria = input('Enter the criteria to search(name/unit_price/amount):')
            value = input('Enter the value:')
            searchProducts(criteria, value)
        elif choice == '3':
            showAllProducts(DB_PATH)
        elif choice == '4':
            print('Bye bye!')
            break
        else:
            print('Error input! Please enter a number from 1 to 4!\n')
            print('---------------------------------------')
        
    
