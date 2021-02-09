def combi(n, k):
    k = min(k, n-k)
    a = 1
    b = 1
    for i in range(n-k+1, n+1):
        a = a * i
    for j in range(1, k+1):
        b = b * j
    return a//b

n = int(input())
a = n // 2
anw = 0
for i in range(1, a+1):
    b = i + (n - i*2)
    anw += combi(b, i)
print((anw+1)%10007)