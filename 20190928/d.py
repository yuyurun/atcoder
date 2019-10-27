import math

A, B = map(int, input().split())

g = math.gcd(A, B)

ya = []
for i in range(2, int(g/2+1)+1):
    if g % i == 0:
        k = [1 for y in ya if i % y==0]
        if len(k) == 0:
            ya.append(i)

k = [1 for y in ya if g % y==0]
if len(k) == 0:
    ya.append(g)

print(len(ya) + 1)
