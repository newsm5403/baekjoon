import sys

def gcd(m, n):
    while n != 0:
        t = m%n
        (m, n) = (n, t)
    return abs(m)

T = int(sys.stdin.readline().rstrip())
for i in range(T):
    A, B = list(map(int, sys.stdin.readline().split()))
    a, b = A, B

    G = gcd(a, b)
    a = a // G
    b = b // G
    L = G*a*b
    print(L)
