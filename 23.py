# Non-abundant sums

# A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.
# A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.
# As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper LIMIT cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this LIMIT.
# Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.

from eulerlib import Divisors

LIMIT  = 28123
div = Divisors(LIMIT)

def sum_of_div(n:int):
    lista = div.divisors(n)
    lista.pop()
    return sum(lista)

num_abudant = []

for i in range(12,LIMIT+1):
    if sum_of_div(i) > i:
        num_abudant.append(i)

sum_abudant = [False] * LIMIT


for i in num_abudant:
    for j in num_abudant:
        if i+j < LIMIT:
            sum_abudant[i+j] = True
        else:
            break


ans  = sum([i for (i,x) in enumerate(sum_abudant) if not x])

print(ans)




