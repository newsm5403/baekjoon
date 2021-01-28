import sys

N = int(sys.stdin.readline().rstrip())
deque = []
while N > 0:
    N -= 1
    command = sys.stdin.readline().split()
    if command[0] == 'push_front':
        deque.insert(0, int(command[1]))
        continue
    elif command[0] == 'push_back':
        deque.append(int(command[1]))
        continue
    elif command[0] == 'pop_front':
        if len(deque) == 0:
            print(-1)
            continue
        a = deque.pop(0)
        print(a)
        continue
    elif command[0] == 'pop_back':
        if len(deque) == 0:
            print(-1)
            continue
        a = deque.pop(-1)
        print(a)
        continue
    elif command[0] == 'size':
        print(len(deque))
        continue
    elif command[0] == 'empty':
        if len(deque) == 0:
            print(1)
        else:
            print(0)
    elif command[0] == 'front':
        if len(deque) == 0:
            print(-1)
            continue
        print(deque[0])
    elif command[0] == 'back':
        if len(deque) == 0:
            print(-1)
            continue
        print(deque[-1])
