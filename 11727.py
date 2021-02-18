n = int(input())
dp = [0] * 1000
dp.insert(0, 1)
dp.insert(1, 3)
for i in range(1, n+1):
    dp[i] = dp[i-1] + 2*dp[i-2]
print(dp[n]%10007)