s = int(input())
l = len(str(s))

ans = 0

for i in range(2**(l-1)):
    su = str(s)[0]
    for j in range(l-1):
        if i & (1<<j) > 0:
            ans += int(su)
            su = str(s)[j+1]
        else:
            su += str(s)[j+1]
    ans += int(su)

print(ans)
