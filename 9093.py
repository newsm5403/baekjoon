import sys

T = int(sys.stdin.readline().rstrip())
for i in range(T):
    lst = list(sys.stdin.readline().split())
    for j in lst:
        for k in reversed(j):
            print(k, end="")
        print(" ", end="")
    print()