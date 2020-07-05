from operator import itemgetter
n,k = map(int, input().split())
aaa = list(map(int, input().split()))
a2 = []
ans = 1
for i in range(n):
    a2.append((aaa[i]**2,aaa[i]))
a2 = sorted(a2, key=itemgetter(0),reverse=True)
print(a2)
a = [a_[1] for a_ in a2]
print(a)
ans = 1
for j in range(k):
    ans *= a[j]

if sum([1 for aa in a[:k] if aa > 0]) % 2 == 0:
    print(ans)
    print(ans%(10**9+7))
else:
    posf = []
    negf = []
    for i in range(n):
        if a[k-1-i] >0:
            if len(posf) == 0:
                posf.append(a[k-1-i])
        else:
            if len(negf) == 0:
                negf.append(a[k-1-i])
        if len(posf)==1 and len(negf) == 1:
            break
    for i in range(n):
        if a[k+i] >0:
            if len(posf) == 1:
                posf.append(a[k+i])
        else:
            if len(negf) == 1:
                negf.append(a[k+i])
        if len(posf)==2 and len(negf) == 2:
            break

    if len(posf)==2 and len(negf) == 2:
        if posf[0]*posf[1] > negf[0]*negf[1]:
            ans /= negf[0]
            ans *= posf[1]
        else:
            ans *= negf[1]
            ans /= posf[0]
    print(ans%(10**9+7))



# マイナスを奇数個選ばざるおえないとき忘れてる

