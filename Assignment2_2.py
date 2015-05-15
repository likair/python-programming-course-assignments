'''
Created on 12.5.2015

    A program which prints out the addition, subtraction and multiplication of two matrices.
    
@author: e1201757
'''
a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
b = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

def matrixPlus(a, b):
    if len(a) == len(b) and len(a[0]) == len(b[0]):
        matrixPrint([[a[i][j] + b[i][j] for j in range(0, len(a[0]))] for i in range(0, len(a))])
#       matrixPrint([[m + n for m, n in zip(i, j)] for i, j in zip(a, b)])
    else:
        print('Illegal!')

def matrixMinus(a, b):
    if len(a) == len(b) and len(a[0]) == len(b[0]):
        matrixPrint([[a[i][j] - b[i][j] for j in range(0, len(a[0]))] for i in range(0, len(a))])
    else:
        print('Illegal!')
def matrixMultiply(a, b):
    if len(a[0]) == len(b):
        c = []
        for i in range(len(a)):
            c.append([])
            for j in range(len(b[0])):
                s = 0
                for k in range(len(b)):
                    s += a[i][k] * b[k][j]
                c[i].append(s)
        matrixPrint(c) 
    else:
        print('Illegal!')       
        
def matrixMultiply2(a, b):
    # if a is a number, b is a matrix
    if isinstance(a, (float, int)) and isinstance(b, (tuple, list)):
        return [[a * i for i in j] for j in b] 
    # if both a and b are matrix
    if isinstance(a, (tuple, list)) and isinstance(b, (tuple, list)):
        return [[sum(map(lambda x: x[0] * x[1], zip(i, j))) for j in zip(*b)] for i in a]  
        
def matrixReverse(a):
    matrixPrint(list(zip(*a)))

def matrixPrint(a):
    for i in range(len(a)):
        for j in range(len(a[0])):
            #format the print number
            print('%3d' %a[i][j], end=' ')
        print()

print('Matrix Plus:')
matrixPlus(a, b)
print('Matrix Minus:')
matrixMinus(a, b)
print('Matrix Multiply1:')
matrixMultiply(a, b)
print('Matrix Multiply2:')
matrixPrint(matrixMultiply2(a, b))
print('Matrix Reverse')
matrixReverse(a)
