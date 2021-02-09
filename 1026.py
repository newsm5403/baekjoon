N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
anw = 0
while len(A) != 0:
    a = min(A)
    b = max(B)
    anw += a*b
    A.remove(a)
    B.remove(b)
print(anw)
