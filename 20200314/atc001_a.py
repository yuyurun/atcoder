# atc001 A

h, w = map(int, input().split())
c = []
for i in range(h):
    c.append(list(input()))
    for j,cc in enumerate(c[-1]):
        if cc == 's':
            s_x = j
            s_y = i
        if cc == 'g':
            g_x = j
            g_y = i


seen = [[0 for i in range(w)] for j in range(h)]
todo = []
seen[s_y][s_x] = 1

for i in range(h*w):
    if s_x-1 >= 0 and seen[s_y][s_x-1] == 0 and c[s_y][s_x-1] != '#':
        todo.append((s_y, s_x-1))
        seen[s_y][s_x-1] = 1
    if s_y-1 >= 0 and seen[s_y-1][s_x] == 0 and c[s_y-1][s_x] != '#':
        todo.append((s_y-1, s_x))
        seen[s_y-1][s_x] = 1
    if s_x+1 < w and seen[s_y][s_x+1] == 0 and c[s_y][s_x+1] != '#':
        todo.append((s_y, s_x+1))
        seen[s_y][s_x+1] = 1
    if s_y+1 < h and seen[s_y+1][s_x] == 0 and c[s_y+1][s_x] != '#':
        todo.append((s_y+1, s_x))
        seen[s_y+1][s_x] = 1
    if len(todo) > 0:
        print(todo)
        print(seen)
        print(s_y,s_x)
        s_y, s_x = todo.pop()
        if s_y == g_y and s_x == g_x:
            print('Yes')
            break
    else:
        print('No')
        break



