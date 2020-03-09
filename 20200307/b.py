n,a,b = map(int, input().split())

m = n//(a+b)
amari = n%(a+b)


print(m*a+min(amari,a))
