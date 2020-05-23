import itertools

n = int(input())
p = list(map(int,input().split()))

ans = []
p += [0]*n

for v in itertools.combinations(p, n):
    ans.append(sum(v))

print(len(set(ans)))
