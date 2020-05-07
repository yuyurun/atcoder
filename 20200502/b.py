x = int(input())
i = 0
total = 100
while x > total:
    total = int(total * 1.01)
    i += 1

print(i)
