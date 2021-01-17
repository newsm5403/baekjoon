n = int(input())
arr = [['*']*n for _ in range(n)]
cnt = 0
v = n
while v!=1:
    v /= 3
    cnt += 1

for cnt in range(cnt):
    idx = [i for i in range(n) if (i // 3 ** cnt) % 3 == 1]
    for i in idx:
        for j in idx:
            arr[i][j] = " "

print('\n'.join([''.join([str(i) for i in row]) for row in arr]))