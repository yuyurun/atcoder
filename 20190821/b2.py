import copy
N, K = map(int, input().split())
P = list(map(int, input().split()))

print(N)
print(K)
print(P)


ans = 0
an_l = []
for i in range(N-K+1):
    print(P[i:i+K])
    print(sorted(P[i:i+K]))
    print(P[i+1:i+K])
    print(sorted(P[i+1:i+K]))
    #if P[i:i+K] != sorted(P[i:i+K]):
    P2 = copy.deepcopy(P)
    P2[i:i+K] = sorted(P2[i:i+K])
    if P2 not in an_l:
        an_l.append(P2)       

print(an_l)
print(len(an_l))
