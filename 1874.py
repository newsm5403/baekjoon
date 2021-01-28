import sys

n = int(sys.stdin.readline().rstrip())
lst = []
stack = [0]
anw = []
for i in range(n):
    lst.append(int(sys.stdin.readline().rstrip()))
for i in range(1, lst[0]+1):
    stack.append(i)
    anw.append('+')
i = stack[-1] + 1
while True:
    if stack[-1] < lst[0]:
        for j in range(i, lst[0] + 1):
            stack.append(j)
            anw.append('+')
        i = stack[-1] + 1
    elif stack[-1] == lst[0]:
        stack.pop(-1)
        lst.pop(0)
        anw.append('-')
    elif stack[-1] > lst[0]:
        anw = ['NO']
        break
    if len(lst) == 0:
        break
print(*anw, sep="\n")
       