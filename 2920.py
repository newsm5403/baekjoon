import sys

N = list(map(int, sys.stdin.readline().split()))
p = N[0]
anw = ''
for i in range(len(N)-1):
    if N[0] > N[-1]:
        anw = 'descending'
        if N[i+1] == N[i] - 1:
            p += N[i+1]
        else:
            print('mixed')
            break
    else:
        anw = 'ascending'
        if N[i+1] == N[i] + 1:
            p += N[i+1]
        else:
            print('mixed')
            break
if p == 36:
    print(anw)
