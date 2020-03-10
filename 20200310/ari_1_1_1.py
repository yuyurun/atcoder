n, b = map(int, input().split())
a = [0] + [int(input()) for i in range(n)]

p = []
for i in range(len(a)):
    for j in range(i+1):
        pair = a[i] + a[j]
        if pair <= b:
            p.append(pair)

p.sort()
ans = 0
import bisect
for i in p:
    r = bisect.bisect_right(p, b-i)
    tmp = i + p[r-1]
    ans = max(tmp, ans)


print(ans)
