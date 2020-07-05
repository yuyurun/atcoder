
n = int(input())
a = list(map(int, input().split()))


so = sorted(a)

ans = 0
if n%2==1:
    ans += so[-(n//2)-1]
ans += so[-1]
ans += sum(so[-(n//2):-1])*2
print(ans)
