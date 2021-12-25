# Summation of primes
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.

from eulerlib import prime_numbers as pm

print(sum(pm.primes(2000000)))