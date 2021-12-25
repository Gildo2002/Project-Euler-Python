# 10001st prime
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10 001st prime number?

def is_primo(val):
    for n in range(2,val):
        if val % n == 0:
            return False
    return True

lim = 0
i = 2

while lim < 10001:
    if is_primo(i):
        lim += 1
    i+=1

print(i)