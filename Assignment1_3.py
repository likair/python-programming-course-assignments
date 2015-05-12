'''
Created on May 12, 2015

@author: Likai
'''
'''
A program which prints all prime numbers smaller than 10000. 
'''

def isPrime(num):
    if num == 1:
        return False
    elif num > 2:
        # for i in range(2,int(num**0.5)+1):
        for i in range(2, num):
            if(not (num % i)):
                return False
    return True

for num in range(1, 10000):
    if(isPrime(num)):
        print(num)
