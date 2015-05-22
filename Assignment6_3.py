'''
Created on 20.5.2015

    A program in which you define regular expressions, which match the following data formats. 
    Test the program and make sure that it works correctly.  
    1. international phone numbers like, +358-40-1345678 
    2. social security numbers, like 120570-467W
    3. numbers less than 1000
    4. date expressions in which we have the month name, day and year, like: Jan. 1. 2014, Feb. 27. 1996 and Mar. 15. 2010

@author: e1201757
'''
import re
PHONE_NUMBER = '+358-40-1345678'
SOCIAL_SECURITY_NUMBERS = '120570-467W'
NUMBER_LT_1000 = '-999.5637'
DATE = 'Jan. 1. 2014'

phoneNumberReg = re.compile(r'\+\d{3}-\d{2}-\d{7}')
socialSecurityNumbersReg=re.compile(r'\d{6}-\d{3}[A-Z]')
numberLt1000Reg = re.compile(r'-\d+\.?\d*|\d{1,3}')
dateReg = re.compile('[A-Z][a-z]{2}\. \d{1,2}\. \d{4}')

if __name__ == '__main__':
    if phoneNumberReg.match(PHONE_NUMBER):
        print('Match!')
    else: 
        print('No match!')
        
    if socialSecurityNumbersReg.match(SOCIAL_SECURITY_NUMBERS):
        print('Match!')
    else: 
        print('No match!')
        
    if numberLt1000Reg.match(NUMBER_LT_1000):
        print('Match!')
    else: 
        print('No match!')
        
    if dateReg.match(DATE):
        print('Match!')
    else: 
        print('No match!')
    
    
    