n, m, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))


ll = [(0, 0, 0)]
ans = 0

while len(ll) > 0:
    c, an, bn = ll.pop()
    if an < n:
        if c+a[an] <= k:
            ll.append((c+a[an], an+1, bn))
        elif an + bn > ans:
            ans = an+bn

    if bn < m:
        if c+b[bn] <= k:
            ll.append((c+b[bn], an, bn+1))
        elif an + bn > ans:
            ans = an+bn
    if an + bn > ans:
        ans = an+bn
        
    ll = list(set(ll))
    print(ll)

print(ans)
