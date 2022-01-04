import sys, heapq
heap = []
N = int(input())
for _ in range(N):
    a = int(sys.stdin.readline().rstrip())
    if a == 0:
        if len(heap) > 0:
            print(-heapq.heappop(heap))
        else:
            print(0)
    else:
        heapq.heappush(heap, -a)