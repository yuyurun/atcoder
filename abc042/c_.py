n, k = map(int, input().split())
d = list(input().split())

while 1:
    if all(dd not in str(n) for dd in d):
        print(n)
        break
    n = n+1
