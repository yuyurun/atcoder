import math
n = int(input())

r = int(math.sqrt(n))

a = 1
b = n

for i in range(1,r+1):
    if n % i == 0:
        a = i
        b = n/i
print(int(a+b-2))
