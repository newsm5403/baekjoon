import sys

def getsum(lst, H):
    sum = 0
    for i in lst:
        if i > H:
            sum += i - H
    return sum

N, M = list(map(int, sys.stdin.readline().split()))
lst = list(map(int, sys.stdin.readline().split()))
anw = []
left = 1
right = max(lst)
while left <= right:
    mid = (left + right) // 2
    sum = getsum(lst, mid)
    print(sum, mid, left, right)
    if sum < M:
        right = mid - 1
    else:
        left = mid + 1

print(right)