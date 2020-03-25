money = 300

# 1,2,3で引き出せるからタプルなのかな
item = (("みかん", 100), ("りんご", 200), ("ぶどう", 300))
n = len(item)
ans = 0

for i in range(2**n):
    bag = []
    for j in range(n):
        if (i >> j) & 1:
            bag.append(item[j][1])
    if sum(bag) <= money:
        ans += 1

print(ans)
