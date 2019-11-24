A,B,X = map(int,input().split())

if X >= A*1000000000+B*10:
    print(1000000000)
else:
    for i in range(X//(A+B),1000000000):
        if X < A*i+B*len(str(i)):
            break
    if i==X//(A+B):
        print(0)
    else:
        print(i-1)
