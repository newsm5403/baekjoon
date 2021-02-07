import sys
import time
N = int(sys.stdin.readline().rstrip())
start = time.time()
anw = [0, 1]
for i in range(N-1):
    anw.append((anw[0] + anw[1])%1000000007)
    anw.pop(0)
if N == 0:
    print(0)
else:
    print(anw[-1] % 1000000007)
print(time.time()-start)