s = input()
t = input()
 
f = False
for i in range(len(s)-(len(t)-1)):
    f = True
    for j in range(len(t)):
        if s[-(j+i+1)] != t[-(j+1)] and s[-(j+i+1)] != '?':
            f = False
    if f == True:
        s = s[:-(len(t)+i)] + t + s[len(s)-1-i:0]
        s = s.replace('?','a')
        print(s)
        break
 
if f == False:
    print('UNRESTORABLE')
