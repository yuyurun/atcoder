n = int(input())
import numpy as np

def num_divisors_table(n):
    table = [0] * (n + 1)

    for i in range(1, n + 1):
        for j in range(i, n + 1, i):
            table[j] += 1

    return table

nlist = np.array(num_divisors_table(n))
ilist = np.array([i for i in range(n+1)]).T
print(sum(nlist*ilist))
