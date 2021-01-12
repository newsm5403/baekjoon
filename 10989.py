import sys

N = int(sys.stdin.readline().rstrip())
a = [0] * 10001
for i in range(N):
    tmp = int(sys.stdin.readline().rstrip())
    a[tmp] += 1
for j in range(len(a)):
    if a[j] > 0:
        for k in range(a[j]):
            print(j)