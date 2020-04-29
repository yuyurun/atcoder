
s = input()

ans = 0
f = 0
end = [0 for i in range(len(s))]


for i in range(len(s)-3):
    st = s[i]+s[i+1]+s[i+2]
    for j in range(len(s)-3-i):
        st += s[i+3+j]
        if int(st)%2019 == 0:
            plus = 1 + end[i+3+j-1]
            ans += plus
            end[i+3+j] += plus
            break
print(ans)
