while True:
    stack = 0
    a = input()
    if a == '0':
        break
    for i in range(len(a)//2):
        if a[i] == a[len(a)-i-1]:
            stack += 1
            continue
        else:
            print('no')
            break
    if stack == len(a) // 2:
        print('yes')
    