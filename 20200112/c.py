n,m = map(int, input().split())

wc = [0 for i in range(n)]
ac = [0 for i in range(n)]

n_wc = 0
n_ac = 0

for i in range(m):
    num,j = input().split()
    num = int(num)

    if j == 'AC' and ac[num-1] == 0:
        n_ac += 1
        ac[num-1] = 1
        n_wc += wc[num-1]
    else:
        wc[num-1] += 1

print(n_ac,n_wc)
