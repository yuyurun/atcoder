n, b = map(int, input().split())

a = [0]
for i in range(n):
    a.append(int(input()))
ans = 0
for i in range(len(a)):
    for j in range(i+1):
        for k in range(j+1):
            for l in range(k+1):
                if a[i] + a[j] + a[k] + a[l] < b and a[i] + a[j] + a[k] + a[l] > ans :
                    ans = a[i] + a[j] + a[k] + a[l] 


    




print(ans)
