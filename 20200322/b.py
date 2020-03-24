s = input()
l = len(s)

f = 'Yes'
for i in range(int((l-1)/2)):
    if s[i] != s[l-i-1]:
        f = 'No'
for i in range(int(((l-1)/2)//2)):
    if s[i] != s[l-i-int((l-1)/2+1)-1]:
        f = 'No'




print(f)
