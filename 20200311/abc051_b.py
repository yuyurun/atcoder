k,s = map(int,input().split())

ans = 0
b = []
for i in range(k+1):
    for j in range(k+1):
        if i + j <= s:
            b.append(i+j)
            
for i in b:
    for j in range(k+1):
        if i + j == s:
            ans += 1
            break
print(ans)
