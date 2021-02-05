import sys
prime_number = [False]+[False]+[True]*1000000
for i in range(2, int(1000000**0.5)+1):
    if prime_number[i] == True:
        for j in range(i+i, len(prime_number), i):
            prime_number[j] = False

T = int(sys.stdin.readline().rstrip())
for i in range(T):
    count = 0
    N = int(sys.stdin.readline().rstrip())
    a = 0
    for j in range((N//2 + 1)):
        if prime_number[j] and prime_number[N-j]:
            count += 1
    print(count)