def prime_number(A, B):
    lst = [False, False] + [True] * (B-1)
    for i in range(2, int(B**0.5) + 1):
        if lst[i] == True:
            for j in range(2*i, B + 1, i):
                lst[j] = False
    lst = lst[A:]
    return lst

A, B, D = list(map(int, input().split()))
primelist = prime_number(A, B)
lst = []
count = 0
for i in range(len(primelist)):
    if primelist[i]:
        lst.append(i+A)

for i in lst:
    if str(D) in str(i):
        count += 1
print(count)