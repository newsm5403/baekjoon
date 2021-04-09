N = int(input())
left = 0
right = N-1
while right > left:
    mid = (left + right) // 2
    if mid*mid >= N:
        right = mid
    else:
        left = mid + 1
print(right)