n = int(input())
x = input()

bbb=x.count('1')
bn = int(x, 2)

for i in range(n):
    waru = bbb
    count = 0
    if x[i] == '1':
        num = bn - 2**(n-i-1)
        waru -= 1
    else:
        num = bn + 2**(n-i-1)
        waru += 1

    while waru != 0:
        num = num%waru
        waru = str(bin(num)).count('1')
        count += 1
    print(count)

