n, m, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

ans = 0
bb = 0
for i in range(len(a)-1):
    s = sum(a[0:len(a)-i])
    if s <= k:
        if ans < len(a)-i:
            ans = len(a)-i
        s = s + sum(b[0:bb])
        bbb = bb
        for j in range(bbb, len(b)):
            s = s + b[j]
            bb = j+1
            if s <= k:
                if ans < len(a)-i+j+1:
                    ans = len(a)-i+j+1
            else:
                break

print(ans)
