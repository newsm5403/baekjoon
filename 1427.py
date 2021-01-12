N = input()
lst = []
for i in N:
    lst.append(int(i))
lst = sorted(lst)
lst = reversed(lst)
for j in lst:
    print(j, end="")