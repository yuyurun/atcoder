h = int(input())
w = int(input())
n = int(input())

s = max(h,w)
if n%s==0:
    print(int(n/s))
else:
    print((n//s)+1)
