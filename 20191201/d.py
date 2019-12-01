n = int(input())
s = input()

ans = n*(n-1)*(n-2)/6


for i in range(0,9):
    f = -1
    for j in range(n):
        if int(s[j]) == i:
            if f == -1:
                f = j
            elif f < 1:
                ans -= (n-j-1)*(n-j-1-1)/2
                f = j
            elif f < 2:
                ans -= f * (n-j-1)
                ans -= (n-j-1)*(n-j-1-1)/2
                f = j
            else:
                ans -= f * (n-j-1)
                ans -= f*(f-1)/2 
                ans -= (n-j-1)*(n-j-1-1)/2
                f = j 


print(int(ans))

