
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