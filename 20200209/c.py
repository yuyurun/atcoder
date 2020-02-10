n = int(input())
a = list(map(int, input().split()))

ans = 'YES'
for i in range(n):
    for j in range(i+1,n):
        if a[i] == a[j]:
            ans = 'NO' 
        


print(ans)
