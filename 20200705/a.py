n = int(input())
if n%1000==0:
    print(0)
else:
    n = 1000 - (n-n//1000*1000)


    print(n)
