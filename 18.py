#Maximum path sum 1
# By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.

# 3
# 7 4
# 2 4 6
# 8 5 9 3

# That is, 3 + 7 + 4 + 9 = 23.

# Find the maximum total from top to bottom of the triangle below:


file = open('Input/18.txt','r')

lista= []

for line in file:
    a = line.split(' ')
    lista.append( [int(i) for i in a])

suma = 0

for i in reversed(range(len(lista) - 1)):
    for j in range(len(lista[i])):
        lista[i][j] += max(lista[i+1][j],lista[i+1][j+1])

print(lista[0][0])