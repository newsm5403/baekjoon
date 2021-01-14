import sys

N = int(sys.stdin.readline().rstrip())
lst = []
score = [1 for _ in range(N)]
for i in range(N):
    lst.append(list(map(int, sys.stdin.readline().split())))
for i in range(len(lst)):
    for j in range(len(lst)):
        if i == j:
            continue
        else:
            if lst[i][0] < lst[j][0] and lst[i][1] < lst[j][1]:
                score[i] += 1
print(*score)