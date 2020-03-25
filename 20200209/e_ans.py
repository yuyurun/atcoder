n = int(input())
k = int(input())

a= n
for i in range(101):
    a = a/10
    if a<=1:
        kai = i
        break
print(kai)

if k == 1:
    if n < 10:
        print(n)
    else:
        print(9*kai+n//(10**kai))
elif k ==2:
    if n<10:
        print(0)
    elif n<100:
        print(n-10-(n//10-1))
    elif n<100:
        print(81+(n//10-1)*9*2+n/10-1)
    else:
        l = [1,2,3,4,5,6,7,8,9,10,20,30,40,50,60,70,80,90,100,200,300,400,500,600,700,800,900]
        for ll in l:
            if ll > n%1000:
                ind = l.index(ll)
        print(81*(kai*(kai-1)/2)+(n//10-1)*9*(kai+1)+ind)

else:
    if n<100:
        print(0)
    else:
        print('aaaaa')


