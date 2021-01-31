import sys

while True:
    lst = [0 for _ in range(4)]
    N = sys.stdin.readline().rstrip('\n')
    if not N:
        break
    for i in N:
        if 65 <= ord(i) <= 90:
            lst[1] += 1
        elif 97 <= ord(i) <= 122:
            lst[0] += 1
        elif 48 <= ord(i) <=57:
            lst[2] += 1
        elif i == ' ':
            lst[3] += 1
    print(*lst)
