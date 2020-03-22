import sys
sys.setrecursionlimit(500*500)
h,w = map(int,input().split())
hw = []
for i in range(h):
    hw.append(input())

todo = [(0,0)]
seen = [[200 for j in range(w)] for i in range(h)]
sx = 0
sy = 0
if hw[0][0] == '.':
    seen[0][0] = 0
else:
    seen[0][0] = 1




while len(todo)>0:
    sx,sy = todo.pop(0)
    if sx + 1 < w and seen[sx+1][sy] == 200:
        todo.append((sx+1,sy))
    if sx + 1 < w and hw[sx+1][sy] == '.' and seen[sx+1][sy] > seen[sx][sy]:
        seen[sx+1][sy] = seen[sx][sy]
    if sx + 1 < w and hw[sx+1][sy] == '#' and seen[sx+1][sy] > seen[sx][sy]+1 and hw[sx][sy] == '.':
        seen[sx+1][sy] = seen[sx][sy]+1
    if sx + 1 < w and hw[sx+1][sy] == '#' and seen[sx+1][sy] > seen[sx][sy] and hw[sx][sy] == '#':
        seen[sx+1][sy] = seen[sx][sy]
    if sy+1 < h and seen[sx][sy+1] == 200:
        todo.append((sx,sy+1))
    if sy + 1 < h and hw[sx][sy+1] == '.' and seen[sx][sy+1] > seen[sx][sy]:
        seen[sx][sy+1] = seen[sx][sy]
    if sy + 1 < h and hw[sx][sy+1] == '#' and seen[sx][sy+1] > seen[sx][sy]+1 and hw[sx][sy] == '.':
        seen[sx][sy+1] = seen[sx][sy]+1
    if sy + 1 < h and hw[sx][sy+1] == '#' and seen[sx][sy+1] > seen[sx][sy] and hw[sx][sy] == '#':
        seen[sx][sy+1] = seen[sx][sy]
    print(todo)
    print(seen)    



print(hw)
print(seen[h-1][w-1])
