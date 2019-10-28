n, k = map(int, input().split())
d = list(input().split())

f = True
while(1):
    n_str = str(n)
    print('aaaaaa')
    for i in range(len(n_str)):
        if n_str[-i-1] in d:
            f = False
            break
    if f == True:
        break
    else:
        n = n-1
print(n)
