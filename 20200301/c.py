n,m = map(int,input().split())
s = []
c = []

ans = ['0' for i in range(n)]
f = True
for i in range(m):
    ss,cc = map(int,input().split())
    for l,o in enumerate(s):
        if s[l] == ss and c[l] != cc:
            f = False
    if ss == 1 and cc == 0 and n != 1:
        f = False
    s.append(ss)
    c.append(cc)

for i,o in enumerate(s):
    ans[o-1] = str(c[i])

if ans[0] == str(0) and n!=1:
    ans[0] = str(1)

if f == False:
    print('-1')
else:
    print(''.join(ans))
