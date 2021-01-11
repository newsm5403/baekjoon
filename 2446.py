N = int(input())
for i in range(N):
    print(' '*i, '*' * (2*N-2*i-1), sep='')
for j in range(1, N):
    print(' '*(N-j-1), '*' * (2*j + 1), sep='')