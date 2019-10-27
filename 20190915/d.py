import numpy as np


n,m = map(int,input().split())
a = np.array(list(map(int,input().split())))
for i in range(m):
    a[a.argmax()] = a[a.argmax()]//2 
print(np.sum(a))
