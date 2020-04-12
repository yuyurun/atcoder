import itertools
import math
k = int(input())
a = [i for i in range(1,k+1)]

ans = 0
for i in itertools.combinations_with_replacement(a,3):
    if i[0] == i[1] and i[1]==i[2]:
        ans += math.gcd(i[2],math.gcd(i[0],i[1]))
    elif i[0] == i[1] or i[1]==i[2] or i[2]==i[0]:
        ans += (math.gcd(i[2],math.gcd(i[0],i[1]))*3)
    else:
        ans += (math.gcd(i[2],math.gcd(i[0],i[1]))*6)


print(ans)
