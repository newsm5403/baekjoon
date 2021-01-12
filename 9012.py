def count(lst):
    count1, count2 = 0, 0
    for i in range(len(lst)):
        if lst[i] == '(':
            count1 += 1
        else:
            count2 += 1
    if count1 == count2:
        return True
    else:
        return False

def tmp(lst):
    tmp = 0
    for j in range(len(lst)):
        if lst[j] == '(':
            tmp += 1
        else:
            tmp -= 1
        if tmp < 0:
            return False
    return True

T = int(input())
for _ in range(T):
    lst = input()
    if count(lst) and tmp(lst):
        print("YES")
    else:
        print("NO")