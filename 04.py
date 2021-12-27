# Largest palindrome product
# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

resp = 0
lim = 1000

for i in range(1,lim):
    for j in range(1,lim):
        if str(i*j) == ''.join(reversed(str(i*j))) and resp < i*j:
            resp = i*j
            print(i,j)

print(resp)