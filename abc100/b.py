d,n = map(int,input().split())
 
if d == 0:
    if n == 100:
        print(101)
    else: 
        print(n)
else:
    if n == 100:
        print(pow(100,d)*(n+1)) 
    else:
        print(pow(100,d)*n)
