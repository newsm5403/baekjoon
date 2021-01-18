import sys
def gcd(a, b):
    r = a % b
    a, b = b, r
    if r == 0:
        return int(a)
    else:
        return gcd(a, b)

t = int(input())

for i in range(t):
    anw = 0
    n = list(map(int, sys.stdin.readline().split()))
    for j in range(1, n[0]):
        for k in range(j+1, n[0]+1):
            anw += gcd(n[j], n[k])
    print(anw)
