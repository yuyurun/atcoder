n, b = map(int, input().split())

a = [0]
for i in range(n):
    a.append(int(input()))

ans = 0
for i1 in a:
    for i2 in a:
        for i3 in a:
            for i4 in a:
                if i1 + i2 + i3 + i4 < b and i1 + i2 + i3 + i4 > ans :
                    ans = i1 + i2 + i3 + i4 


    




print(ans)
