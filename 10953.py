import sys

T = int(sys.stdin.readline().rstrip())
for i in range(T):
    lst = sys.stdin.readline().strip()
    A = lst[0:1]
    B = lst[2:]
    print(int(A) + int(B))