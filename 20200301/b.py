a = [0 for i in range(9)]
c = [0 for i in range(9)]
a[0],a[1],a[2] = map(int,input().split())
a[3],a[4],a[5] = map(int,input().split())
a[6],a[7],a[8] = map(int,input().split())

n = int(input())
for i in range(n):
    b= int(input())
    for j in range(9):
        if a[j] == b:
            c[j] = 1

print(c)

ans = 'No'
for i in range(3):
    if c[3*i]+c[3*i+1]+c[3*i+2] == 3:
        ans = 'Yes'

for i in range(3):
    if c[i]+c[3+i]+c[6+i] == 3:
        ans = 'Yes'

if c[0]+c[4]+c[8] == 3:
    ans = 'Yes'
if c[2]+c[4]+c[6] == 3:
    ans = 'Yes'

print(ans)
