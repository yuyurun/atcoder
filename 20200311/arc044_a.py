import math
n = int(input())

x = []
y = []
for i in range(n):
    xx, yy = map(int, input().split())
    x.append(xx)
    y.append(yy)

ans = 0
for i in range(n):
    for j in range(i):
        jo = math.pow(x[i]-x[j],2) + math.pow(y[i]-y[j],2)
        if jo > ans:
            ans = jo

print(math.sqrt(ans))




'''
# 累乗
math.pow(3,2) → 3**2
math.sqrt(3,2) → 3**0.5

# x y をn行受け取る
xy = [tuple(map(int, input().split())) for _ in range(n)]
xy[1][2]みたいに使う

'''
