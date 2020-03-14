import math
n = int(input())

ans = []
d = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
fa = math.factorial(n)+1
for i in range(math.factorial(n)):
    tu = 'a'
    for j in range(2, n+1):
        if len(set(tu)) 
        for k in range(j):
            hh = i % j
            if hh < k+1 and hh >= k:
                tu += d[k]
    ans.append(tu)

for i in range(n):
    for j, jj in enumerate(ans):
        if not d[i] in jj:
            for k in range(i+1, n):
                if d[k] in jj:
                    ans[j] = jj.replace(d[k], d[i])
                    break
print('\n'.join(sorted(set(ans))))
