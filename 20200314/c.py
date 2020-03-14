a,b,c = map(int, input().split())

l = (c-a-b)**2
r = 4*a*b

if c-a-b<0:
    print('No')
elif l>r:
    print('Yes')
else:
    print('No')
