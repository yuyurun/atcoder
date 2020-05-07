n,k = map(int, input().split())
a = [1 for i in range(n)]
for i in range(k):
    d = int(input())
    aa = input().split()
    for k in aa:
        a[int(k)-1] = 0

print(sum(a))
