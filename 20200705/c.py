import itertools
h,w,k = map(int, input().split())
c = []
for i in range(h):
    a = input()
    for j in range(w):
        if a[j] == '#':
            c.append((i,j))

ans = 0

sel = ['h'+str(i) for i in range(h)]
sel += ['w'+str(i) for i in range(w)]
for m in range(h+w):
    for v in  itertools.combinations(sel,m):
        count = [1 for kk in range(len(c))]
        for vv in v:
            if vv[0]=='h':
                for e,(i,j) in enumerate(c):
                    if i == int(vv[1]):
                        count[e] = 0
            if vv[0]=='w':
                for e,(i,j) in enumerate(c):
                    if j == int(vv[1]):
                        count[e] = 0
        if sum(count) == k:
            ans += 1
        

print(ans)
