import sys

N = int(sys.stdin.readline().rstrip())
anw = [[]*i for i in range(200)]
lst = []
for i in range(N):
    lst = list(sys.stdin.readline().split())
    anw[int(lst[0]) - 1].append(lst[1])
for j in range(len(anw)):
    if anw[j] == []:
        continue
    else:
        for k in range(len(anw[j])):
            print(j+1, anw[j][k], end="\n")