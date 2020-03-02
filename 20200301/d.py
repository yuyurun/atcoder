n,m,k = map(int,input().split())
f = []
b = []

for i in range(m):
    ss,cc = input().split()
    f.append(ss)
    f.append(cc)

for i in range(k):
    ss,cc = input().split()
    b.append(ss)
    b.append(cc)

ans = []
for i in range(n):
    hh = ' '.join(f)
    print(hh)
    print(i+1)
    print(hh.count(str(i+1)))
    print(' '.join(b))
    print(' '.join(b).count(str(i+1)))
    ans.append(str(n-1-(' '.join(f)).count(str(i+1))-(' '.join(b)).count(str(i+1))))

print(' '.join(ans))
