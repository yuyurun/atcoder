import copy
S = list(input())
K = int(input())


a = S[0]
c = 0
S2 = copy.deepcopy(S)
for i in range(1, len(S)):
    if S2[i] == S2[i-1]:
        S2[i] = '1'
        c += 1

a = S[-1]
last = 0
for i in range(2, len(S)+1):
    last += 1
    if S[-i] != a:
        break

if all([e == S[0] for e in S[1:]]) == True:
    if len(S)%2==0:
        print(int(len(S)/2*K))
    else:
        print(int(len(S)//2*((K+1)//2)+(len(S)//2+1)*(K//2)))
elif S[0] == S[-1] and last % 2 == 1:
    c3 = 0
    S3 = copy.deepcopy(S)
    for i in range(2, len(S)):
        if S3[i] == S3[i-1]:
            S3[i] = '1'
            c3 += 1
    print(c + (c3+1)*(K-1))
else:
    print(c*K)
