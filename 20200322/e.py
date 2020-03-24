hh,ww,k = map(int,input().split())
start = []
from collections import deque
import copy

whi = 0
for i in range(hh):
    start.append(input())
    whi += start[-1].count('1')
if whi > k:
    ss = deque([(start,whi)])
else:
    ss = []

co = 0
print(ss)
while ss:
    s,wh = ss.popleft()
    w = len(s[0])
    h = len(s)
    a = 0
    co += 1
    for i in range(w):
        for j in range(h):
            if s[j][i]=='1':
                a += 1

        if wh/2 <= a:
            ai = i
            break

    b = 0
    for i in range(h):
        b += s[i].count('1')
        if wh/2 <= b:
            bi = i
            break

    if a<b:
        if a > k:
            s2 = copy.deepcopy(s)
            for i in range(h):
                s2[i] = s[i][:ai+1]
            ss.append((s2,a))
            if wh -a > k:
                for i in range(h):
                    s[i] = s[i][ai+1:]
                ss.append((s,wh-a))
    else:
        if b > k:
            ss.append((s[:bi+1],b))
            if wh - b > k:
                ss.append((s[bi+1:],wh-b))


    print(s)
    print(ss)

print(co)














