x,y,a,b,c = map(int, input().split())
p = list(map(int, input().split()))
q = list(map(int, input().split()))
r = list(map(int, input().split()))

p =sorted(p)[::-1][:x][::-1]
q =sorted(q)[::-1][:y][::-1]
r =sorted(r)[::-1][:x+y]


pp = 0
qq = 0
for rr in r:
    if p[pp]<rr or q[qq]<rr:
        if p[pp]<q[qq]:
            p[pp] = rr
            pp += 1
        else:
            q[qq] = rr
            qq +=1

print(sum(p)+sum(q))

