from typing import no_type_check


import numpy as np

array = np.loadtxt('13.txt',dtype=str)

for i in array:
    sum = 0
    for j in range(len(i)):
        sum += int(i[j])
        print(sum)
    print(sum)

