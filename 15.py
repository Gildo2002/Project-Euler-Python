# Lattice paths
# Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.
# How many such routes are there through a 20×20 grid?

from math import factorial as fac

n = 40
lista = []

for j in range(n+1):
            lista.append(fac(n)//(fac(j) * fac(n-j)))
print('Routes: ', max(lista))