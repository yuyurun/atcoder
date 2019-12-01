t1,t2 = map(int,input().split())
a1,a2 = map(int,input().split())
b1,b2 = map(int,input().split())

if t1*a1+t2*a2 == t1*b1+t2*b2:
    print('infinity')
else:
    if t1*a1+t2*a2 < t1*b1+t2*b2:
        allb = t1*b1+t2*b2
        alls = t1*a1+t2*a2
        tb = t1*b1
        ts = t1*a1
    else:
        alls = t1*b1+t2*b2
        allb = t1*a1+t2*a2
        ts = t1*b1
        tb = t1*a1
    
    print(ts-tb)
    print(allb-alls)
    print((ts-tb)//(allb-alls))
