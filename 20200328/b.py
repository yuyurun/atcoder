n = int(input())

ans = 0

ans += (n//500)*1000
ans += ((n%500)//5)*5

print(ans)

