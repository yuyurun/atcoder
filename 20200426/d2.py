s = input()
import time
start = time.time()
ans = 0
f = 0
for i in range(len(s)-3):
    st = s[i]+s[i+1]+s[i+2]
    for j in range(len(s)-3-i):
        st += s[i+3+j]
        if f > 0 :
            f -= 1
        else:
            if int(st)%2019 == 0:
                ans += 1
                print(i,j+i+3)
                f = 3

print(time.time()-start)
print(ans)
