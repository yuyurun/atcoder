n = int(input())
x = []
l = []
c = []
d = {}

for i in range(n):
    xx,ll = map(int, input().split())
    x.append(xx)
    l.append(ll)
    d[xx] = ll


dct = sorted(d.items())

print(dct)
f = 0
ans = 0
f = dct[0][0] + dct[0][1]
for i in range(1,len(dct)):
    if f > dct[i][0] - dct[i][1]:
        ans += 1
        f = min(f,dct[i][0]+dct[i][1])
    else:
        f = dct[i][0]+dct[i][1]
        
    print(f)
    print(ans)

print(n-ans)
