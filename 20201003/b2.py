n,s = input().split()

n = int(n)


ans = 0
for l in range(n-1):
    for rr in range(1,int((n-l)/2)+1):
        

        print('========')

        flag = True
        r = rr*2+l-1

        print(l,rr,r)
        for i in range(rr):
            print('ss',l+i,r-i)
            print(s[3])
            if s[l+i] == s[r-i]:
                flag = False

        '''
        for i in range(int((r-l+1)/2)):
            if s[l+i] != dic[s[r-i]]:
                flag = True
        '''
        if flag == True:
                print('waao')
                print(l,r)
                ans += 1

print(ans)
