A, B, X = map(int, input().split())

if X >= A*1000000000+B*10:
    print(1000000000)
elif X < A*1+B*1:
    print(0)
else:
    under = 0
    over = X
    while(over-under>1):
        mid = (over+under)//2
        if A*mid+B*len(str(mid))<=X:
            under = mid
        else:
            over = mid

    print(under)
