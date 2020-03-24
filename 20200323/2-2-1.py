a = int(input())
coin = [500,100,50,10,5,1]

a = 1000-a
ans = 0
for c in coin:
    ans += a//c
    a = a%c

print(ans)

