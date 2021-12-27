

import numpy as np

array = np.loadtxt('13.txt',dtype=str)
sum = 0

for i in array:
        sum += int(i)

print(str(sum)[0:10])