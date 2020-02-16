n,k = map(int,input().split())
a = list(map(int, input().split()))

seil = []
ful = []
zero = 0

for i in a:
    if i < 0:
        ful.append(i)
    elif i > 0:
        seil.append(i)
    else:
        zero += 1
sei = len(seil)
seil.sort(reverse=True)
ful.sort()
print(seil)
print(ful)


fi = 0
si = 0
if k <= sei*(n-sei-zero):
    for i in range(max(sei,len(ful))):
    print()
elif k <= sei*(n-sei-zero)+zero*(n-zero):
    print(0)
else:
    print(n)
