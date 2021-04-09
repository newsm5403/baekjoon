N = int(input())
dp = [1, 1]
anw = [4]
for i in range(1, N):
    dp.append(dp[i-1]+dp[i])
    anw.append(anw[i-1]+dp[i]*2)
print(anw[-1])
