'''
Created on 12.5.2015

@author: e1201757
'''
a = [[1, 2, 3], [4, 5 , 6], [7, 8, 9]]
b = [[1, 2, 3], [4, 5 , 6], [7, 8, 9]]

def matrixPlus(a, b):
    if(len(a) == len(b) and len(a[0]) == len(b[0])):
        c=[[0]*len(a)]*len(a[0])
        for i in range(0, len(a)):
            for j in range(0, len(a[0])):
                c[i][j] = a[i][j] + b[i][j]
        matrixPrint(c)
    else:
        print('Illegal!')

def matrixMinus(a, b):
    if(len(a) == len(b) and len(a[0]) == len(b[0])):
        c=[[0]*len(a)]*len(a[0])
        for i in range(0, len(a)):
            for j in range(0, len(a[0])):
                c[i][j] = a[i][j] - b[i][j]
        matrixPrint(c)
    else:
        print('Illegal!')
        
def matrixPrint(a):
    for i in range(0, len(a)):
        for j in range(0, len(a[0])):
            print(str(a[i][j]) , end=' ')
        print()



print('Matrix Plus:')
matrixPlus(a, b)
print('Matrix Minus:')
matrixMinus(a, b)
