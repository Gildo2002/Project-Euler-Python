# Smallest multiple
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

import os
os.environ["CUDA_VISIBLE_DEVICES"] = "0"

lim = 20
value = 2
num = 0

while True:
    for i in range(1,lim + 1):
        if value % i == 0:
            num +=1
    if num == lim:
        print(value)
        break
    else:
        value += 1
        num = 0
    print(value)