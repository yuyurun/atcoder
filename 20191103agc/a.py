s = input()

ans = 0
f = 0
be = 0
for k in range(len(s)):
    if s[k] == '<':
        if f != 0 and be != 0:
            ans -= be * f
            be = 0
        ans += be + 1
        f = 0
        be += 1
    elif be ==0:
        f += 1
        ans += be + f
    else:
        f += 1
        ans += be - 1
        be = be - 1
    print(k,be,f,ans)
print(ans)
