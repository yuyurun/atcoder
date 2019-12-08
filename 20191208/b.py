s = input()

count = 0
for i in range(int((len(s)+1)/2)):
    if s[i] != s[len(s)-i-1]:
        count += 1

print(count)
