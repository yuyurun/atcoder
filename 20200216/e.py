n = int(input())

a = []

for i in range(len(str(n))):
    a.append(int(str(n)[i]))
size = len(a)


if a[-1] > 5:
    print(sum(a[:size-1])+1+(10-a[-1]))
 
    #print(sum(a[:size-1])+1+(10-a[-1])-9+1)




