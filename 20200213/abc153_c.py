n,k = map(int,input().split())
h = list(map(int,input().split()))

if n<k :
    print(0)
else:
    print(sum(sorted(h)[:n-k]))
