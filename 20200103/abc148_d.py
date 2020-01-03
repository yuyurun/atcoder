n = int(input())
a = map(int,input().split())

count = 1 
for i in a:
    if i == count:
        count += 1
print(n-count+1)
