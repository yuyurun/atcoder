import math
n = int(input())

ans = []
d = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

todo = ['a']
while len(todo)>0:
    p = todo.pop(-1)
    l = len(p)
    cou = len(set(p))
    if l < n:
        for i in range(cou+1):
            todo.append(p+d[i])
    else:
        ans.append(p)


print('\n'.join(sorted(set(ans))))
