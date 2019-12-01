A, B, X = map(int, input().split())

if X >= A*1000000000+B*10:
    print(1000000000)
elif X//B < 10:
    c = 0
    for i in range(X//B):
        if X >= A*(X//B-i)+B*len(str(X//B-i)):
            c = X//B-i
            break
    print(c)
else:
    c = 0
    for i in range(X//A):
        if X >= A*(X//A-i)+B*len(str(X//A-i)):
            c = X//A-i
            break
    print(c)
