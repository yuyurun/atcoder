n = input()
a = list(map(int,input().split()))

suma = 0
lena = len(a)

sum_a = [a[i]^a[j] for j in range(i+1,len(a)) for i in range(lena-1)]

for i in range(len(a)-1):
    for j in range(i+1,len(a)):
        suma += a[i]^a[j]
        print(suma)
print(suma%(10**9+7))
print(sum(sum_a)%(10**9+7))
