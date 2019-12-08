n = int(input())

TF = [-1 for i in range(n)]
Fset = []
l = [[-1 for j in range(n)] for i in range(n)]
for i in range(n):
    lena = int(input())
    for j in range(lena):
        x, y = map(int, input().split())
        l[i][x-1] = y

for i in range(n):
    for j in range(n):
        if i != j:
            if l[i][j]+l[j][i] == 1:
                TF[i] = 0
                TF[j] = 0
            if l[i][j]+l[j][i] == 0:
                Fset.append((i, j))
            for k in range(n):
                if l[i][j] >= 0 and l[i][j] != l[i][k]:
                    Fset.append((j,k))


print(Fset)
