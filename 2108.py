import sys
def average(lst):
    avg = sum(lst) / len(lst)
    return round(avg)

def frequency(lst):
    tmp = []
    dp = [1] * len(lst)
    for i in range(len(lst)-1):
        if lst[i] == lst[i+1]:
            dp[i+1] += dp[i]
    maxfre = max(dp)
    for i in range(len(dp)):
        if dp[i] == maxfre:
            tmp.append(lst[i])
    
    if len(tmp) > 1:
        return tmp[1]
    else:
        return tmp[0]

N = int(sys.stdin.readline())
lst = []
anw = []
for i in range(N):
    lst.append(int(sys.stdin.readline()))
lst.sort()

anw.append(average(lst))
anw.append(lst[len(lst)//2])
anw.append(frequency(lst))
anw.append(lst[-1]-lst[0])
for i in anw:
    print(i)
