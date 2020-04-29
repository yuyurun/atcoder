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
    if pf == True and qf == True and  p[pp]<rr and q[qq]<rr:
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
    elif pf == True and p[pp]<rr:
            if pf == True:
               p[pp] = rr
               pp += 1
               if pp == x:
                  pf = False
    elif pf == True and q[qq]<rr:
            if qf == True:
                q[qq] = rr
                qq +=1
                if qq == y:
                    qf = False
print(sum(p)+sum(q))




