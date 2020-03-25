n = int(input())
x = []
l = []
c = []

for i in range(n):
    xx,ll = map(int, input().split())
    x.append(xx)
    l.append(ll)
    


ans = 0
f = 0
for i in range(1,n):
    if x[i]-x[i-1] < l[i]+l[i-1]:
        f += 1
    else:
        ans += (f+1)//2
        f = 0

    print(f,ans)
if f != 0:
    ans += (f+1)//2

print(n-ans)
