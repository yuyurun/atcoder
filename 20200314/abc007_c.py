r, c = map(int, input().split())

sy, sx = map(int, input().split())
gy, gx = map(int, input().split())

cc = []
for i in range(r):
    cc.append(list(input()))


todo = []
seen = [[-1 for i in range(c)] for j in range(r)]
sy = sy-1
sx = sx-1
seen[sy][sx] = 0

for i in range(r*c):
    if sy-1 >= 0 and seen[sy-1][sx] == -1 and cc[sy-1][sx] == '.':
        todo.append((sy-1,sx))
        seen[sy-1][sx] = seen[sy][sx]+1
    if sx-1 >= 0 and seen[sy][sx-1] == -1 and cc[sy][sx-1] == '.':
        todo.append((sy,sx-1))
        seen[sy][sx-1] = seen[sy][sx]+1
    if sy+1 < r and seen[sy+1][sx] == -1 and cc[sy+1][sx] == '.':
        todo.append((sy+1,sx))
        seen[sy+1][sx] = seen[sy][sx]+1
    if sx+1 < c and seen[sy][sx+1] == -1 and cc[sy][sx+1] == '.':
        todo.append((sy,sx+1))
        seen[sy][sx+1] = seen[sy][sx]+1

    if len(todo)>0:
        sy, sx = todo.pop(0)
    else:
        break
print(seen[gy-1][gx-1])
