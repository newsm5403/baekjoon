import math
N = int(input())
lst = []
if N == 0:
    print(0)
else:    
    while N != 0:
        lst.insert(0, abs(N%(-2)))
        N = math.ceil(N/(-2))
    print(*lst, sep="")