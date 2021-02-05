N = int(input())
N = [i for i in range(1, N+1)]
i = 0
while len(N) != 1:
    if len(N) % 2 == 0:
        d = []
        for i in range(1, len(N), 2):
            d.append(N[i])
        N = d
    elif len(N) % 2 == 1:
        d = []
        for i in range(1, len(N), 2):
            d.append(N[i])
        d.append(d.pop(0))
        N = d
print(*N)
