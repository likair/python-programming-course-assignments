'''
Created on 12.5.2015

@author: e1201757
'''
'''
foo=0
print([x[:] for x in [[foo]*10]*10])

a = [[1, 2, 3], [4, 5 , 6], [7, 8, 9]]
c=[[0]*len(a)]*len(a[0])
print(c)
'''
'''
matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
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
'''
'''
a = [1, 2, 3, 4, 5]
b = [1, 2, 3, 4, 5]

for i, j in zip(a, b):
    print(str(i) + ' ' + str(j))

print([(i, j) for i, j in zip(a, b)])
'''
'''
matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
print(*matrix)
print(list(zip(*matrix)))
'''
'''
a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
b = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
c = []
for i in range(0, len(a)):
    c.append([])
    for j in range(0, len(a[0])):
        c[i].append(a[i][j] + b[i][j])
print(c)
'''
'''
a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
b = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
#c = list([0] * len(a[0])) * len(a)
#c = [0] * len(a[0])
#c = [[0] * len(a[0])] * len(a)
#d = c * 3
#d = list(c) * 3
c = [[0]*3]*3
#print(c)
for i in range(len(c)):
    for j in range(len(c[0])):print(c[i][j], end=' ')
    print()
'''
'''
a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
b = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
c = [[0] * len(a)] * len(a[0]) # the mistake is here, because ... the copy lists will be changed as the first one
#c = [[0, 0, 0], [0, 0, 0], [0, 0, 0]] # This is the right way
#c = [i[:] for i in [[0] * len(a)] * len(a[0])] # This is the right way too
print('the initial state:')
print(c)
print()
time = 0
for i in range(len(a)):
    for j in range(len(a[0])):
        time +=1
        c[i][j] = a[i][j] + b[i][j]
        print('the ' + str(time) + ' time')
        print('c[' + str(i) + '][' + str(j) +'] = ' + str(c[i][j]))
        print(c)
        print()
print('the final result:')
print(c)
'''
'''
a = [[0] * 3] * 3
print(a)
a[0][0] = 1
print(a)
'''
'''
print([i[:] for i in [[0]*3]*3])
'''



