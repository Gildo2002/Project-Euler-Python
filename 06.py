# Sum square difference
# The sum of the squares of the first ten natural numbers is 385
# The square of the sum of the first ten natural numbers is 3025
# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 2640
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

import math

sum_cuad = 0
lim = 100

for i in range(1,lim + 1):
    sum_cuad += i**2

cuad_sum = sum(range(1,lim + 1)) ** 2

print(cuad_sum - sum_cuad)