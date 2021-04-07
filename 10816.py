import sys

N = int(sys.stdin.readline().strip())
lst = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline().strip())
card = list(map(int, sys.stdin.readline().split()))
anw = [0] * M
lst.sort()

def front(num, lst):
    left = 0
    right = len(lst) - 1
    while right > left:
        mid = (left + right) // 2
        if lst[mid] >= num:
            right = mid
        else:
            left = mid + 1
    return right

def back(num, lst):
    if lst[N-1] == num:
        return N
    left = 0
    right = len(lst) - 1
    while right > left:
        mid = (left + right) // 2
        if lst[mid] > num:
            right = mid
        else:
            left = mid + 1
    return right
for i in range(M):
    front_ = front(card[i], lst)
    back_ = back(card[i], lst)
    anw[i] = back_ - front_
print(*anw)