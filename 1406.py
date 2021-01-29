import sys

stk = list(sys.stdin.readline().rstrip())
stk2 = []
M = int(sys.stdin.readline().rstrip())
while M > 0:
    M -= 1
    command = sys.stdin.readline().split()
    if command[0] == 'L':
        if stk: stk2.append(stk.pop())
        else: continue
    elif command[0] == 'D':
        if stk2: stk.append(stk2.pop())
        else: continue
    elif command[0] == 'B':
        if stk: stk.pop()
        else: continue
    elif command[0] == 'P':
        stk.append(command[1])

print(''.join(stk + stk2[::-1]))