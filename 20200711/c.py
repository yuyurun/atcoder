n = int(input())

ans = [0 for i in range(n)]
for i in range(1,105):
    for j in range(i,105):
        for k in range(j,105):
            if i*i + j*j + k*k + i*j + k*j + i*k > n:
                break
            print(i,j,k)
            print(i*i + j*j + k*k + i*j + k*j + i*k)
            if i == j and j==k:
                ans[i*i + j*j + k*k + i*j + k*j + i*k-1] = 1
            elif i == j or j==k or k==i:
                ans[i*i + j*j + k*k + i*j + k*j + i*k-1] = 3
            else:
                ans[i*i + j*j + k*k + i*j + k*j + i*k-1] = 6

print('\n'.join(map(str,ans)))

