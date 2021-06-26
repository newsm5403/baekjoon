def prime_number():
    prime_number = [False, False] + [True] * 10000002
    for i in range(2, 10000002):
        if prime_number[i] == True:
            for k in range(2*i, 10000002, i):
                prime_number[k] = False
    return prime_number

A, B = list(map(int, input().split()))
count = 0
lst = prime_number()
for i in range(2, 10000002):
    j = 2
    if i*i > B:
        break
    if lst[i]:
        while True:
            if A <= pow(i, j) <= B:
                count += 1
                j += 1
            elif pow(i, j) > B:
                break
            else:
                j += 1
print(count)
