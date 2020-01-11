n = int(input())
a = list(map(int,input().split()))

new = sorted(a)

for i in range(n-2):

    if new[i+1] == a[i]:
        tmp = new[i+1]
        new[i+1] = new[i+2]
        new[i+2] = tmp

print(' '.join(new))
    
