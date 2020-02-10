import copy
n,k = map(int, input().split())
p = list(map(int, input().split()))

max_set = [0]
for i in range(n-k+1):
    pair = []
    for j in range(k):
        pair.append(p[i+j])
    if sum(max_set) < sum(pair):
        max_set = copy.copy(pair)

ans = 0
for i in max_set:
    ans += (i+1)/2
print(ans)
