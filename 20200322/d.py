n = int(input())
a = list(map(int, input().split()))
import collections
c = collections.Counter(a)


al = 0
for v in c.values():
    al += v*(v-1)/2


for aa in a:
    print(int(al - c[aa]+1))


