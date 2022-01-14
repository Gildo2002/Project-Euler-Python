# Longest Collatz sequence
# The following iterative sequence is defined for the set of positive integers:

# n → n/2 (n is even)
# n → 3n + 1 (n is odd)

# Using the rule above and starting with 13, we generate the following sequence:

# 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

# Which starting number, under one million, produces the longest chain?

# NOTE: Once the chain starts the terms are allowed to go above one million.

lim = 1000000
long_seq = 0
step = 0
x = 0

def collatz(n):
    cant = 1
    while n != 1:
        if n % 2 == 0:
            n = n /2
        else:
            n = 3 * n + 1
        cant += 1
    return cant

for i in range(1,lim + 1):
    step = collatz(i)
    if step > x:
        long_seq = i
        x = step

print(long_seq)