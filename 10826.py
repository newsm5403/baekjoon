import sys

N = int(sys.stdin.readline().rstrip())
anw = [0, 1]
for i in range(N-1):
    anw.append(anw[i] + anw[i+1])
if N == 0:
    print(anw[0])
else:
    print(anw[-1])