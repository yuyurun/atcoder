h, w, a, b = map(int, input().split())
li1 = str(1)*a+str(0)*(w-a)
li2 = str(0)*a+str(1)*(w-a)
for _ in range(h-b):
    print(li1)
for _ in range(b):
    print(li2)
