n,m,q = map(int, input().split())

import itertools
a = []
for i in range(q):
    a.append(input().split())

suma = sum([int(aa[3]) for aa in a])

ans = 0
l = [i for i in range(m)]
for v in itertools.combinations_with_replacement(l, n-1):
    ans_ = 0
    v = [0]+list(v)
    print(v)
    for j in range(q):
        if v[int(a[j][1])-1] - v[int(a[j][0])-1] == int(a[j][2]):
            ans_ += int(a[j][3])
    if ans_ > ans:
        ans = ans_
        if ans == suma:
            break
print(ans)


