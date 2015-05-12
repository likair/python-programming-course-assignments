'''
Created on 12.5.2015

@author: e1201757
'''
'''

c=[[0]*len(a)*len(a[0])]
print(c)

foo=0
print([x[:] for x in [[foo]*10]*10])

a = [[1, 2, 3], [4, 5 , 6], [7, 8, 9]]
c=[[0]*len(a)]*len(a[0])
print(c)
'''

matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], ]
#0
print(list(zip(*matrix)))
#1
print([[row[i] for row in matrix] for i in range(4)])
#2
transposed = []
for i in range(4):
    transposed.append([row[i] for row in matrix])
print(transposed)
#3
transposed = []
for i in range(4):
    # the following 3 lines implement the nested listcomp
    transposed_row = []
    for row in matrix:
        transposed_row.append(row[i])
    transposed.append(transposed_row)
print(transposed)


