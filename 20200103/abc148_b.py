n = int(input())
s,t = input().split()
ans = [s[i]+t[i] for i in range(n)]

print(''.join(ans))
