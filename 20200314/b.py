h,w = map(int, input().split())

if h ==1 or w==1:
    print(1)
elif h%2 == 1 and w%2==1:
    print(((h+1)//2)*w-w//2)
elif h%2 ==0:
    print((h//2) * w)
else:
    print((w//2) * h)

