n = int(input())
a = list(map(int,input().split()))

g = [i/2 for i in a if i%2==0]
print(g)
print(int(sum(g)))
