n = int(input())
s = input()

rc = s.count('R')
gc = s.count('G')
bc = s.count('B')

ans = rc*gc*bc

for i in range(n):
    if s[i] == 'R':
        for j in range(1,min(n-i-1, i)+1):
            if s[i-j] != s[i+j] and s[i-j] != 'R' and s[i+j] != 'R':
                ans -= 1
        for j in range(1,int((n-i-1)/2)+1):
            if s[i+2*j] != s[i+j] and s[i+2*j] != 'R' and s[i+j] != 'R':
                ans -= 1
        for j in range(1,int(i/2)+1):
            if s[i-j] != s[i-2*j] and s[i-j] != 'R' and s[i-2*j] != 'R':
                ans -= 1

print(ans)
