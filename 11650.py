import sys

N = int(sys.stdin.readline().rstrip())
lst = [] 
for i in range(N):
    lst.append(list(map(int, sys.stdin.readline().split())))
lst.sort()
for i in lst:
    print(*i)