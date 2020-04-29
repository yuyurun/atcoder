n,x,y = map(int, input().split())

for i in range(1,n):
    ans = n-i
    if i < max(x-y,y-x):
        ans += (x-1)
    if i > n-max(x-y,y-x):
        ans -= (x-1)
    print(ans)


