n = int(input())
p = list(map(int,input().split()))

MAX = 10000
dp = [1] + [0]*MAX

for v in p:
    for j in range(MAX, v-1, -1):
        dp[j] |= dp[j-v]

print(sum(dp))
