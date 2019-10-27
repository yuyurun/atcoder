import copy
N, K = map(int, input().split())
P = list(map(int, input().split()))

ans = 0
an_l = []
for i in range(N-K+1):
    P2 = copy.deepcopy(P)
    P2[i:i+K] = sorted(P2[i:i+K])
    if P2 not in an_l:
        an_l.append(P2)       

an_l = [P[0:i]+sorted(P[i:i+K])+P[i+K:] for i in range(N-K+1) if P[0:i]+sorted(P[i:i+K])+P[i+K:] not in an_l]
print(len(an_l))
