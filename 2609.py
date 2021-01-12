import sys

A, B = list(map(int, sys.stdin.readline().split()))
a, b = A, B

def gcd(m, n):
    while n != 0:
        t = m%n
        (m, n) = (n, t)
    return abs(m)
G = gcd(a, b)
a = a // G
b = b // G
L = G*a*b
print(G)
print(L)
