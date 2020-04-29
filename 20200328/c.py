k,n = map(int, input().split())
a = list(map(int, input().split()))

max_l = k-a[-1]+a[0]


for i in range(1,n):
    if a[i] - a[i-1] > max_l:
        max_l = a[i] - a[i-1]



print(k-max_l)
