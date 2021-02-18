N = int(input())
dp = [0 for i in range(N)]
dp.insert(1, 1)
for i in range(2, N+1):
    a = int(i**0.5)
    dp[i] = dp[i - a*a] + 1
    for j in range(2, a):
        if dp[i] > dp[i - j*j] + 1:
            dp[i] = dp[i - j*j] + 1
print(dp[-1])