
N = int(input())
a = list(map(int,input().split()))

d = [0]*N
for i,j in enumerate(a):
    d[j-1] = str(i+1)

print(' '.join(d))
