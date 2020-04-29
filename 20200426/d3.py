import time
start = time.time()

s = input()

ans = 0
f = 0
end = [0 for i in range(len(s))]

m = 0
st = ''
l = 0
while l < len(s):
    st += s[l]
    if int(st)%2019 == 0:
        if m > 0:
            ans += m+1
        else:
            ans += 1
        st = ''
    else:
        m = 0
    l += 1


print(time.time()-start)
print(ans)
