n = int(input())
a = list(map(int, input().split()))
count = 0
for i,aa in enumerate(a):
    if i %2 == 0 and aa%2==1:
        count += 1
print(count)
