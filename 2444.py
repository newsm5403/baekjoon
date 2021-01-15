import sys

N = int(sys.stdin.readline().strip())
for i in range(N):
    print(' '*(N-i-1), '*'*(2*i + 1), sep="")
for j in reversed(range(1, N)):
    print(' '*(N-j), '*'*(2*j - 1), sep="")