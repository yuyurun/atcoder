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


for i in range(h*w):
    for k in range(i+1,h*w):
        jj = i%w
        ii = i//w
        ll = k%w
        kk = k//w
        print(k,w,k%w)
        print(i,k)
        print(ii,jj,kk,ll)
        if s[ii][jj] == '.' and s[kk][ll] == '.':
        #if s[ii-1][jj-1] == '.' and s[kk-1][ll-1] == '.':
            d_min = bfs(ii,jj,kk,ll)
            if d_max < d_min:
                d_max = d_min
print(d_max)
