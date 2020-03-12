abcd = input()
l = len(abcd)

ans = ''
for i in range(2**(l-1)):
    s = int(abcd[0])
    tasi = abcd[0]
    for j in range(l-1):
        if i & 1<<j > 0:
            s += int(abcd[j+1])
            tasi += '+' + abcd[j+1]
        else:
            s -= int(abcd[j+1])
            tasi += '-' + abcd[j+1]
    if s == 7:
        ans = tasi + '=7'
print(ans)


