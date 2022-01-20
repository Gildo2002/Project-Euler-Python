# Amicable numbers
# Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
# If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

# For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

# Evaluate the sum of all the amicable numbers under 10000.

from eulerlib import primes
from eulerlib import Divisors
from numpy import number


def divisores(value:int):
    lista = div.divisors(value)
    if len(lista) > 1:
        lista.pop()
    return lista

n = 10000
prime = primes(n)
div = Divisors(n)
number = []
sum_div = []
suma = 0

for i in range(2,n):
    if i not in prime:
        number.append(i)

for a in number:
    i = sum(divisores(a))
    b = sum(divisores(i))
    if (a == b and i > a ):
        suma += a + i

print(suma)