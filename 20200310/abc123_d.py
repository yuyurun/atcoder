x, y, z, k = map(int,input().split())
a =list(map(int,input().split()))
b =list(map(int,input().split()))
c =list(map(int,input().split()))


ab = []
for aa in sorted(a)[::-1][:k]:
    for bb in sorted(b)[::-1][:k]:
        ab.append(aa+bb)

ab = sorted(ab)[::-1][:k]

ans = []
for aabb in ab:
    for cc in sorted(c)[::-1][:k]:
        ans.append(aabb+cc)

for ansi in sorted(ans)[::-1][:k]:
    print(ansi)
