K = int(input())
lst = [0, 1]
for i in range(2, K+1):
    lst.append(lst[i-2] + lst[i-1])
if K == 1:
    print(0, 1)
else:
    print(lst[K-1], lst[K])