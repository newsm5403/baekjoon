def nCk(n,k):
    a = 1
    b = 1
    for i in range(k):
        a *= n - i
        b *= i + 1
    return a // b

R, C, W = map(int, input().split())
anw = 0
for i in range(W):
    for j in range(i+1):
        anw += nCk(R+i-1, C+j-1)
print(anw)