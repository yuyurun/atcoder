
s = input()

ans = 0
f = 0
end = [0 for i in range(len(s))]
m = 0
i = 0

while i <len(s)-3:
    st = s[i]+s[i+1]+s[i+2]
    for j in range(len(s)-3-i):
        st += s[i+3+j]
        if int(st)%2019 == 0:

            plus = 1 + end[i-1]
            ans += plus
            end[i+3+j] = end[i+3+j]+ plus
            i = i+j+3-1
            break
    i += 1
print(ans)
