n, k = map(int, input().split())
n = n -1
a = 1
b = 1
for i in range(k - 1):
    a *= n - i
    b *= i + 1
print(a//b)