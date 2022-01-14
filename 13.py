# Large Sum
# Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.

import numpy as np

array = np.loadtxt('13.txt',dtype=str)
sum = 0

for i in array:
        sum += int(i)

print(str(sum)[0:10])