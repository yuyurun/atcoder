import collections
n = list(map(int,input().split()))

a = [int(input()) for i in range(n[2])]
kk = n[1]-n[2]


counter = collections.Counter(a)

for i in range(n[0]):
    if kk+counter[i+1] <= 0:
        print('No')
    else:
        print('Yes')
