s = input()
t = input()

ans = []
for i in range(len(s)-(len(t)-1)):
    f = True
    for j in range(len(t)):
        if s[j+i] != t[j] and s[j+i] != '?':
            f = False
    if f == True:
        s2 = s[:i] + t + s[i+len(t):]
        s2 = s2.replace('?','a')
        ans.append(s2)

        

if len(ans) > 0:
    print(min(ans))
else:
    print('UNRESTORABLE')

        
