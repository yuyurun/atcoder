import collections

n = int(input())
a = list(map(int, input().split()))

c = collections.Counter(a)

for i in range(n):
    print(c[i+1])


