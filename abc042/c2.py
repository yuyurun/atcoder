n,k = input().split()
d = list(input().split())

ans = ''

for i in range(10):
    if not str(i) in d:
        sm = str(i)
        break

for i in range(len(str(n))):
    if n[i] in d:
        co = str(int(n[i])+1)
        while(1):
            if not co in d:
                break
            co = co + 1
        ans = ans + co + sm*(len(n)-i-1)
        break
    else:
        ans = ans + n[i]
print(ans)


