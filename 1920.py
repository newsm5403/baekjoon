import sys

N = int(sys.stdin.readline().rstrip())
A = set(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline().rstrip())
B = list(map(int, sys.stdin.readline().split()))

for l in B:
    if l in A:
        print(1)
    else:
        print(0)