N, K = map(int, input().split())
lst = [i for i in range(1, N+1)]
stk = []
a = 0
for i in range(N):
    a =(a + K-1)%len(lst)
    stk.append(lst.pop(a))
print('<', end="")
print(*stk, sep=', ', end="")
print('>', end="")
