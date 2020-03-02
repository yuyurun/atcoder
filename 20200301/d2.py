n,m,k = map(int,input().split())
f = []
b = []
s = []
fr = [[] for i in range(n)]
for i in range(m):
    ss,cc = input().split()
    fr[int(ss)-1].append(cc)
    fr[int(cc)-1].append(ss)
    fla =False
    for su in s:
        if ss in su:
            su.append(ss)
            su.append(cc)
            fla = True
        elif cc in su:
            su.append(ss)
            su.append(cc)
            fla = True
    if fla == False:
        s.append([ss,cc])

print(s)
        


bl = [[] for i in range(n)]
for i in range(k):
    ss,cc = input().split()
    bl[int(ss)-1].append(cc)
    bl[int(cc)-1].append(ss)
    


ans = []


for i in range(n):
    anss = 0
    print('yaru'+str(i+1))
    for su in s:
        if str(i+1) in su:
            fff = su
    for kouho in set(fff):
        print(kouho)
        print(bl[i])
        print(fr[i])
        if not str(kouho) in bl[i]:
            if not str(kouho) in fr[i] :
                anss += 1
        print(bl[i].count(str(kouho)))
        print(fr[i].count(str(kouho)))

    ans.append(str(anss-1))

print(' '.join(ans))
