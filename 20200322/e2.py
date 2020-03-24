h,w,k = map(int,input().split())
s = []


wh = 0
for i in range(h):
    s.append(input())
    wh += s[-1].count('1')

co = 0

while wh > k:
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
        for i in range(h):
            s[i] = s[i][:ai+1]
        w = ai+1
        wh = a
    else:
        s = s[:bi+1]
        h = bi+1
        wh = b

    print(s)

print(co)














