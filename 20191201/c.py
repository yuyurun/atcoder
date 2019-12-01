x = int(input())

nokori = x%100
max_n = x//100
print(nokori//5 + nokori%5//4 + nokori%5%4//3 + nokori%5%4%3//2 + nokori%5%4%3%2)
if max_n < nokori//5 + nokori%5//4 + nokori%5%4//3 + nokori%5%4%3//2 + nokori%5%4%3%2:
    print(0)
else:
    print(1)
