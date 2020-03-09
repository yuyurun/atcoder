a,b = map(int, input().split())

a_min = a/0.08
a_max = (a+1)/0.08
b_min = b/0.1
b_max = (b+1)/0.1

print(a_min)
print(a_max)
print(b_min)
print(b_max)
if a_min <= b_min:
    if b_min < a_max:
        if int(b_min) == b_min:
            print(int(b_min))
        else:
            print(int(b_min+1))
    else:
        print('-1')
else:
    if a_min < b_max:
        if int(a_min) == a_min:
            print(int(a_min))
        else:
            print(int(a_min+1))
    else:
        print('-1')

