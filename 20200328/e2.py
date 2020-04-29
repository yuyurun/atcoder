x,y,a,b,c = map(int, input().split())
p = list(map(int, input().split()))
q = list(map(int, input().split()))
r = list(map(int, input().split()))

p =sorted(p)[::-1][:x][::-1]
q =sorted(q)[::-1][:y][::-1]
r =sorted(r)[::-1][:x+y]

pp = 0
qq = 0
pf = True
qf = True
for rr in r:
    lll = False
    if pf == True and qf == True:
        if p[pp]<rr and q[qq]<rr:
            lll = True
            if p[pp]<q[qq] and pf == True:
                p[pp] = rr
                pp += 1
                if pp == x:
                    pf = False
            elif qf == True:
                q[qq] = rr
                qq +=1
                if qq == y:
                    qf = False
    if pf == True and lll == False:
        if p[pp]<rr:
            lll = True
            if pf == True:
               p[pp] = rr
               pp += 1
               if pp == x:
                  pf = False
    if qf == True and lll == False:
        if q[qq]<rr:
            lll = True
            if qf == True:
                q[qq] = rr
                qq +=1
                if qq == y:
                    qf = False

print(sum(p)+sum(q))




