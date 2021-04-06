n = int(input())
dp = [1]

for i in range(n):
    a = 0
    for j in range(len(dp)):
        a += dp[j]*dp[i-j]
    dp.append(a)
print(dp[-1])