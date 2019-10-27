import collections
n = int(input())
a = list(map(int,input().split()))


c = collections.Counter(a)
values, counts = zip(*c.most_common())

for i in range(1,n+1):
    ans = n//i
    over = [jj-ans for jj in counts if jj>ans]
    if over != []:
        ans = ans -(sum(over)+i-1)//i

    print(ans)
