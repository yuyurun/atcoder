from collections import deque
h,w = map(int, input().split())
s = [list(input()) for i in range(h)]

d_max = 0


def bfs(sx,sy,gx,gy):
    d = [[float("inf")] * w for i in range(h)]

    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    que = deque([])
    que.append((sx, sy))
    d[sx][sy] = 0

    while que:
        p = que.popleft()
        if p[0] == gx and p[1] == gy:
            break
        for i in range(4):
            nx = p[0] + dx[i]
            ny = p[1] + dy[i]

            if 0 <= nx < h and 0 <= ny < w and s[nx][ny] != "#" and d[nx][ny] == float("inf"):
                que.append((nx, ny))
                d[nx][ny] = d[p[0]][p[1]] + 1

    if d[gx][gy] == float("inf"):
        return 0
    else:
        return d[gx][gy]

for i in range(h):
    for j in range(w):
        for k in range(h):
            for l in range(w):

                d_min = bfs(i,j,k,l)
                if d_max < d_min:
                    d_max = d_min
print(d_max)
