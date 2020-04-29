a,b,c,d = map(int, input().split())

t = (a+d-1)//d
o = (c+b-1)//b

if t >= o:
    print('Yes')
else:
    print('No')
