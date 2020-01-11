n = int(input())

s = []
t = []

for i in range(n):
    a,b = input().split()
    s.append(a)
    t.append(int(b))

x = input()

flag = False
ans = 0

for i in range(n):
    if flag == True:
        ans += t[i]
    if s[i] == x:
        flag = True

print(ans)
