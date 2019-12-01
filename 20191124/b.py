n = int(input())
s = input()

all_ = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

result = ''
for i in range(len(s)):
    for j in range(len(all_)):
        if s[i] == all_[j]:
            result += all_[(j+n)%len(all_)]
            break

print(result)
