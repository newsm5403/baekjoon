import sys

N = int(sys.stdin.readline().rstrip())
lst = set()
anw = [[]*i for i in range(50)]
for i in range(N):
    lst.add(input())
lst = list(lst)
for j in range(1, 51):
    for k in lst:
        if len(k) == j:
            anw[j-1].append(k)
anw = [v for v in anw if v]
for i in anw:
    if len(i) == 1:
        print(*i)
    else:
        i = sorted(i)
        print(*i, sep='\n')
            