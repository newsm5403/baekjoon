def gcd(a, b):
    while b != 0:
        t = a % b
        (a, b) = (b, t)
    return abs(a)

N, S = map(int, input().split())
A = list(map(int, input().split()))
stk = []
anw = []
for i in A:
    stk.append(abs(i-S))
stk = list(set(stk))
a = stk[0]
for i in stk:
    a = gcd(a, i)
print(a)