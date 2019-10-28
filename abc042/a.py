l = list(map(int,input().split()))

s = [5,7,5]
for a in l:
    if a in s:
        s.remove(a)
if s == []:
    print('YES')
else:
    print('NO')
