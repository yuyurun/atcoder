n,k = map(int, input().split())
a = list(map(int, input().split()))

for i in range(k):
    b = [0 for i in range(n)]
    for j in range(n):
        for l in range(1,a[j]+1):
            if j+l < n:
                b[j+l] += 1
            if j-l >= 0:
                b[j-l] += 1
        b[j] += 1
            
    a = [b[i] for i in range(n)]

print(' '.join(map(str,b)))
