# Largest product in a grid
# In the 20×20 grid below, four numbers along a diagonal line have been marked in red.
# The product of these numbers is 26 × 63 × 78 × 14 = 1788696.
# What is the greatest product of four adjacent numbers in the same direction (up, down, left, right, or diagonally) in the 20×20 grid?

import numpy as np

array = np.loadtxt('dato.txt',dtype=int,delimiter=' ')

lim = np.shape(array)[0]
cant = 4
max_num = 0

#Horizontal
for i in range(0,lim):
    for j in range(0, (lim + 1) - cant):
        value = list(map(int,array[i, j:j + cant]))
        if np.prod(value) > max_num:
            max_num = np.prod(value)

#Vertical
for i in range(0,(lim + 1) - cant):
    for j in range(0, lim):
        value = list(map(int,array[i:i + cant,j]))
        if np.prod(value) > max_num:
            max_num = np.prod(value)

#Diagonal - derecha
for i in range(0,(lim + 1) - cant):
    for j in range(0, (lim + 1) - cant):
        value = list()
        for k in range(0,cant):
            value.append((int(array[i+k, j+k])))
        if np.prod(value) > max_num:
            max_num = np.prod(value)

#Diagonal - Izquierda
for i in range(0,(lim + 1 ) - cant):
    for j in range(lim -1 ,cant - 2 , -1):
        value = list()
        for k in range(0,cant):
            value.append((int(array[i+k, j-k])))
        if np.prod(value) > max_num:
            max_num = np.prod(value)

print(max_num)
