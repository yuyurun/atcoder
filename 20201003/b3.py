from itertools import accumulate

n,s = input().split()

n = int(n)


line = []
for i in range(n):
    if s[i] == 'A':
        line.append(-1)
    if s[i] == 'T':
        line.append(1)
    if s[i] == 'C':
        line.append(-1000)
    if s[i] == 'G':
        line.append(1000)

ans = 0
for l in range(n-1):
    for j in accumulate(line[l:]):
        if j == 0:
            ans += 1

print(ans)
