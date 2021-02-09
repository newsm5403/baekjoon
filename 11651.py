N = int(input())
lst = []
for i in range(N):
    a, b = map(int,input().split())
    lst.append([b, a])
lst.sort()
for i in range(len(lst)):
    lst[i][0], lst[i][1] = lst[i][1], lst[i][0]
    print(*lst[i])