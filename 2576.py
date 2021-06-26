lst = [0 for i in range(7)]
sum = 0
lst2 = []
for i in range(7):
    lst[i] = int(input())
for j in range(7):
    if(lst[j] % 2 != 0):
        lst2.append(lst[j])
        sum += lst[j]
if(len(lst2) == 0):
    print(-1)
else:
    print(sum)
    print(min(lst2))