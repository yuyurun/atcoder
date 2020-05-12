n,k = map(int, input().split())
ans = 0
for i in range(10**9):
    if n < k:
        ans = i+1
        break
    n = n//k

print(ans)
