a = [int(input()) for _ in range(9)]
anw = sum(a)
tmp = 0
for i in range(len(a)-1):
    for j in range(i+1, len(a)):
        tmp = a[i] + a[j]
        if anw - tmp == 100:
            a1, a2 = a[i], a[j]
            a.remove(a1)
            a.remove(a2)
            break
a.sort()
for j in a:
    print(j)