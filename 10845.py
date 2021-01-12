import sys

N = int(input())
lst = []
for _ in range(N):
    a = sys.stdin.readline().split()
    if len(a) > 1:
        lst.append(int(a[1]))
    elif a[0] == 'pop':
        if len(lst) == 0:
            print(-1)
        else:
            b = lst.pop(0)
            print(b)
    elif a[0] == 'size':
        print(len(lst))
    elif a[0] == 'empty':
        if len(lst) == 0:
            print(1)
        else:
            print(0)
    elif a[0] == 'front':
        if len(lst) == 0:
            print(-1)
        else:
            print(lst[0])
    elif a[0] == 'back':
        if len(lst) == 0:
            print(-1)
        else:
            print(lst[-1])