n,s = input().split()

n = int(n)

dic = {'A':'T','T':'A','C':'G','G':'C'}

ans = 0
for l in range(n-1):
    for rr in range(1,int((n-l)/2)+1):
        


        flag = True
        r = rr*2+l-1

        for i in range(rr):
            if s[l+i] != dic[s[r-i]]:
                flag = False

        if flag == True:
                ans += 1

print(ans)
