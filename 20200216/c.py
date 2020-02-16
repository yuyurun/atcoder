import collections
n = int(input())
s = []
for i in range(n):
    s.append(input())

c = collections.Counter(s)

ans = []
most = c.most_common()
max_size = most[0][1]
for i in range(len(most)):
    if max_size != most[i][1]:
        break
    else:
        ans.append(most[i][0])

print('\n'.join(sorted(ans)))
