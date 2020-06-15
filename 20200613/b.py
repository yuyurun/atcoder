a,v = map(int, input().split())
b,w = map(int, input().split())
t = int(input())

if v <= w:
    print('NO')
elif ((a-b)/(v-w))**2 <=t**2:
    print('YES')
else:
    print('NO')
