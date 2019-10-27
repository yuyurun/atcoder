a = int(input())

import itertools
import numpy

n =a
b = []
for i in range(2,int(-(-a**0.5//1))+1):
    if a % i ==0:
        b.append(i)
        a = a/i
        while a%i==0:
            b.append(i)
            a = a/i
if a != 1:
    b.append(a)
if b == []:
    b.append(a)

if len(b)==1:
    print(int(b[0]-1))
elif len(b)==2:
    print(int(b[0]+b[1]-2))
# else:
#     r = b[-1]
#     s = b[-2]
#     for j in range(2,len(b)):
#         i = -1-j
#         if r>s:
#             s = s*b[i]
#         else:
#             r = r * b[i]
#     print(int(r+s-2))

else:
    pr = n
    for i in range(1,(len(b)+1)//2):
        for j in list(itertools.combinations(b,i)):
            if pr > numpy.prod(j)+n/numpy.prod(j)-2:
                pr = numpy.prod(j)+n/numpy.prod(j)-2
    print(int(pr))


