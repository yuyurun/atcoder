a,b,n = map(int, input().split())

if b > n:
    x = n
else:
    #x = (n // b)*b-1
    x = b-1
ans = int(a*x/b)-a*int(x/b)
print(x)
print(ans)
