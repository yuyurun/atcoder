n = int(input())


from fractions import Fraction
a = [0]*n
b = [0]*n

for i in range(n):
    a[i],b[i] = map(int,input().split())

c = zip(a,b)
cc = sorted(c)

a,b = zip(*cc)
a = list(a)
b = list(b)


su = 0
ri = 0
win = 0
for i,c in enumerate(a):
    su = sum(a[0:i-1])
    ri = 0
    for j in range(i,n):
        su += a[j]
        ri += b[j]
        if su<ri:
            win += 1
            break

for i in range(2,win+1):
    f = True
    while(1):
        if win % i == 0 and n % i ==0:
            win = win/i
            n = n/i
        else:
            f = False
        if f == False:
            break

print(int(win),int(n))
