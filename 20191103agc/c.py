n = int(input())

from itertools import permutations, combinations

ans = 3**n

for i in range(n/2+1,n+1):
    ans -= 2


print(ans)
