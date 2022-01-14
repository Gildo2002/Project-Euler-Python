# Power digit sum
# 2 ^ 15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

# What is the sum of the digits of the number 2 ^ 1000?

def pow_num(n):
    number = pow(2,n)
    suma = sum( int(i) for i in str(number))
    print(suma)
    pass

pow_num(1000)