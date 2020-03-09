s = input()
n = int(input())
b = ''
a = ''
h = 0
for i in range(n):
    qq = list(input().split())
    if qq[0] == '1':
        h += 1
    else:
        if qq[1] == '1':
            if h % 2 ==1:
                a = a + qq[2]
            else:
                b = qq[2] + b
        else:
            if h % 2 ==1:
                b = qq[2] + b
            else:
                a = a + qq[2]
            
s = b + s + a
if h % 2 ==1:
    s = s[::-1]
print(s)
