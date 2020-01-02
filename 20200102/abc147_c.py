n = int(input())

a = []
deps = []
for i in range(n):
    dep = []
    a.append(int(input()))
    for j in range(a[i]):
        x,y = map(int,input().split())
        dep.append((x, y))
    deps.append(dep)


ans = 0
for i in range(2 ** n):
    bag = 0
    ok = 0
    for j in range(n):
        if (i >> j) & 1:
            bag += 1
            for x,y in deps[j]:
                if (i >> x-1) & 1:
                    if y != 1:
                        ok = -1
                else:
                    if y == 1:
                        ok = -1
    if ok == 0:
        ans = max(ans,bag)

print(ans)
                        


