import sys

T = int(sys.stdin.readline().strip())
lst = []
dp = [[1,0],[0,1]]
for i in range(T):
    lst.append(int(sys.stdin.readline().strip()))
r = max(lst)
for i in range(1, r):
    a = dp[i-1][0] + dp[i][0]
    b = dp[i-1][1] + dp[i][1]
    dp.append([a, b])
for i in range(T):
    print(*dp[lst[i]])
