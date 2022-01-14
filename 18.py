#Maximum path sum 1
# By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.

# 3
# 7 4
# 2 4 6
# 8 5 9 3

# That is, 3 + 7 + 4 + 9 = 23.

# Find the maximum total from top to bottom of the triangle below:

# import numpy as np

# array = np.loadtxt('Input/18.txt',dtype=int,delimiter=' ')

# print(np.shape(array))


file = open('Input/18.txt','r')

lista= []

for line in file:
    a = line.split(' ')
    lista.append( [int(i) for i in a])

suma = 0 

for i in lista:
    suma += max(i)

print(suma)