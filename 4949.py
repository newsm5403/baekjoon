import sys

def check(a):
    j = 0
    stk = []
    for i in range(len(a)):
        if a[i] == '(':
            stk.append(a[i])
        elif a[i] == ')':
            stk.append(a[i])
            if len(stk) < 2:
                return "no"
            if stk[len(stk)-2] == '(':
                stk.pop()
                stk.pop()
        elif a[i] == '[':
            stk.append(a[i])
        elif a[i] == ']':
            stk.append(a[i])
            if len(stk) < 2:
                return "no"
            if stk[len(stk)-2] == '[':
                stk.pop()
                stk.pop()
    if len(stk) == 0:
        return "yes"
    else:
        return "no"
anw = []
while True:
    a = input()
    if a == '.':
        break
    else:
        anw.append(check(a))
for i in anw:
    print(i)
    