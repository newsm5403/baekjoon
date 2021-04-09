import sys

T = int(sys.stdin.readline().strip())
dp = []
for i in range(T):
    a = 1
    N, M = map(int, sys.stdin.readline().split())
    for j in range(N):
        a *= (M - j) / (j + 1)
    dp.append(a)

for k in dp:
    print(round(k))