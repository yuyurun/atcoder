n = int(input())
x = []
l = []
c = []
d = {}
same = 0
bef = -1
bef_l = -1
ans = 0
min_same = 0

for i in range(n):
    xx,ll = map(int, input().split())
    if i > 0:
        if bef == xx:
            same += 1
            min_same = min(min_same,ll)
        else:
            ans += same
            if same > 0:
                d[bef] = min_same
            else:
                d[bef] = bef_l
            same = 0
    bef = xx
    bef_l = ll
    
ans += same
if same > 0:
    d[bef] = min_same
else:
    d[bef] = bef_l
    
dct = sorted(d.items())

print(dct)
f = 0
same = 0
for i in range(1,len(dct)):
    if dct[i][0] == dct[i-1][0]:
        ans += 1
    elif dct[i][0]-dct[i-1][0] < dct[i][1]+dct[i-1][1]:
        f += 1
    else:
        ans += (f+1)//2
        f = 0

    print(ans)

if f != 0:
    ans += (f+1)//2

print(n-ans)
