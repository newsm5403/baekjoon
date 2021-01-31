import sys

S = sys.stdin.readline().rstrip()
lst = [0 for _ in range(26)]
for i in range(len(S)):
    idx = ord(S[i]) - 97
    lst[idx] += 1
print(*lst)