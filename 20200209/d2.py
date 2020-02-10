import copy
n,k = map(int, input().split())
p = list(map(int, input().split()))

max_set = sum(p[:k])
pair = sum(p[:k])
for i in range(n-k):
    pair -= p[i]
    pair += p[i+k]
    if max_set < pair:
        max_set = pair

print((max_set+k)/2)
