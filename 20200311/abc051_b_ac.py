# ABC051 b 全探索 AC
# 2重forでおさめる
k,s = map(int,input().split())

ans = 0
for i in range(k+1):
    for j in range(k+1):
        l = s - i - j
        if l <= k and l >= 0:
            ans += 1
            
print(ans)
