N, K = list(map(int, input().split()))

prime = [False] * N
lst = []
for i in range(2, N+1):
    for j in range(1, N):
        idx = i * j
        if idx > N:
            break
        if prime[idx-1] == False:
            lst.append(idx)
            prime[idx-1] = True
print(lst[K-1])