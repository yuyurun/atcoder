n = int(input())

ans = 0
count = 0
if n % 2 == 0:
    while n > 10:
        ans += 10 ** count
        count += 1
        n = n/10
print(n * (10 ** count))
n = int((n * (10 ** count)%(10 ** count))/10)
print(n)


print(ans+n)
