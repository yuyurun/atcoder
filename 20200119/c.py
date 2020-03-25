n = int(input())
a = list(map(int, input().split()))

min_n = n+1
ans = 0

for aa in a:
    if min_n > aa:
        ans += 1
        min_n = aa

print(ans)
