N, K = map(int, input().split())

K = min(K, N-K)
a = N
b = K
for i in range(1, K):
    a *= N-i
    b *= i
if b == 0:
    anw = 1
else:
    anw = a // b
print(anw) 