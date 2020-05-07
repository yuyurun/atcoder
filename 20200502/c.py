n,m,q = map(int, input().split())

import itertools
a = []
for i in range(q):
    a.append(input().split())

ans = 0
l = [i for i in range(m)]
for v in itertools.combinations_with_replacement(l, n):
    ans_ = 0
    for j in range(q):
        print(v[0])
        print(a[j][2])
        print(v[int(a[j][2])-1] )
        if v[int(a[j][1])-1] - v[int(a[j][0])-1] == int(a[j][2]):
            ans_ += int(a[j][3])
    if ans_ > ans:
        ans = ans_

print(ans)


