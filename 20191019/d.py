n = int(input())
l = list(map(int, input().split()))

l.sort()
l.reverse()
c = 0
f = 0
for i in range(n-2):
    for j in range(i+1, n-1):
        for k in range(j+1, n):
            print(l[i],l[j],l[k])
            if l[i] < l[j]+l[k]:
                c += 1
            else:
                print('********')

                f = 1
                break
        if f ==1:
            f = 0
            break
        

print(c)
