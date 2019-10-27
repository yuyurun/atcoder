N, K = map(int, input().split())
P = list(map(int, input().split()))

print(N)
print(K)
print(P)


ans = 0
for i in range(N-K+1):
    print(P[i:i+K])
    print(sorted(P[i:i+K]))
    print(P[i+1:i+K])
    print(sorted(P[i+1:i+K]))
    if i == 0:
        if P[i:i+K] != sorted(P[i:i+K]):
            ans += 1
    else:
        if P[i+1:i+K] != sorted(P[i+1:i+K]):
            ans += 1


if ans == 0:
    print(1)
else:
    print(ans)
