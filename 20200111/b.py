import math
n = int(input())
x = list(map(int, input().split()))

ans = 0

for i in range(n-1):
    ans += (x[n-1]-x[i])*math.factorial(n-1)
    print(ans)
    if i >0:
        for j in range(n-2):
            ans -= (j+1)*(x[n-1]-x[i])
        print(ans)
    if i > 0 and i < n-2:
        for j in range(n-i-2):
            m =  x[n-1] - x[n-2-j]
            ans -= m
        print(ans)
    print(ans)
    print('-------')

print(ans%(10**9+7))
