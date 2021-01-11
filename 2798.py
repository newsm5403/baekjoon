import sys

N, M = map(int, input().split())
a = list(map(int, sys.stdin.readline().split()))
sum = []
for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            anw = a[i] + a[j] + a[k]
            if anw <= M:
                sum.append(anw)
print(max(sum))