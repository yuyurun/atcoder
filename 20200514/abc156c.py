n = int(input())
x = list(map(int, input().split()))

ans = 1000000
for i in range(1,101):
    e = 0
    for j in x:
        e += (i-j)**2
    if ans > e:
        ans = e

print(ans)
