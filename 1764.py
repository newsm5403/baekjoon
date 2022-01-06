N, M = list(map(int, input().split()))
l = []
s = []
for _ in range(N):
    l.append(input())
for _ in range(M):
    s.append(input())
result = set(l) & set(s)
print(len(result))
result = list(result)
result.sort()
for i in result:
    print(i)