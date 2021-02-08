A, B = map(int, input().split())
m = int(input())
lst = list(map(int, input().split()))
anw = []
a = 0
for i in range(len(lst)):
    a += pow(A, len(lst)-i-1) * lst[i]
while a >= B:
    tmp = a % B
    a = a // B
    anw.insert(0, tmp)
anw.insert(0, a)
print(*anw)