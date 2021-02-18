N = int(input())
lst = list(map(int, input().split()))
dp = [0] * (N+1)
lst.insert(0, 0)
for i in range(1, N+1):
    for j in range(1, i+1):
        if dp[i] > lst[j] + dp[i-j]:
            dp[i] = lst[j] + dp[i-j]
print(dp[-1])