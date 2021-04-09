import sys

n = int(sys.stdin.readline().strip())
left = 0
right = n
while right > left:
    mid = (left + right) // 2
    if mid*mid >= n:
        right = mid        
    else:
        left = mid + 1
print(right)