import sys

N = int(sys.stdin.readline().strip())
lst = list(set(map(int, sys.stdin.readline().split())))
M = int(sys.stdin.readline().strip())
card = list(map(int, sys.stdin.readline().split()))
anw = [0] * M
lst.sort()

for i in range(M):
    left = 0
    right = len(lst) - 1
    while left <= right:  # card에 숫자가 없는 경우도 있기 때문에 강제로 종료시켜준다
        mid = (left + right)//2
        if lst[mid] == card[i]:
            anw[i] = 1
            break
        elif lst[mid] > card[i]:
            right = mid - 1
        else:
            left = mid + 1
print(*anw)