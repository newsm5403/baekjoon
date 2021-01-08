prime_number = [False, False] + [True]*10002
for i in range(2, 10002):
    if prime_number[i] == True:
        for j in range(2 * i, 10002, i):
            prime_number[j] = False

T = int(input())
for i in range(T):
    n = int(input())
    a = n // 2
    b = a
    while a > 0:
        if prime_number[a] and prime_number[b]:
            print(a, b)
            break
        else:
            a -= 1
            b += 1
