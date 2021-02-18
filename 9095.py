T = int(input())
for i in range(T):
    dp = [0] * 10
    dp.insert(0, 1)
    n = int(input())
    for j in range(1, n+1):
        for k in range(1, 4):
            if j-k < 0:
                break
            dp[j] += dp[j-k]
    print(dp[n])