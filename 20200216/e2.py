n = int(input())

a = []
over = []
be = 0
count = 0
f = 0 # 連チャン中
usiro = 0
f4 = 0

for i in range(len(str(n))):
    a.append(int(str(n)[i]))
    if int(str(n)[i])>5:
        if f == 1:
            usiro += 1
        over.append(int(str(n)[i]))
        if f != 1:
            count += 1
        f = 1
    elif int(str(n)[i])==5 and f == 1:
        f = 1
    elif int(str(n)[i])==4 and f == 1:
        f = 1
    else:
        f = 0

size = len(a)

print(sum(a))
print(a)
print(over)
print(sum(over))
print(len(over))
print(count)


print(sum(a)-(2*sum(over))+10*len(over)+count -usiro)

