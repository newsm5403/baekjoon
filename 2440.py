N = int(input())
lst = []
for i in range(N):
    a = int(input())
    lst.append(a)
anw = sorted(lst)
for i in anw:
    print(i)