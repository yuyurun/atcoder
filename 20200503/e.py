n = int(input())
a = list(map(int, input().split()))

ans = 0
for i in range(n):
    for j in range(n-i-a[i]):
        if a[i+j+a[i]] + a[i] == j+a[i] or a[i+j+a[i]] + a[i] == -j-a[i]:
            ans +=1

print(ans)
