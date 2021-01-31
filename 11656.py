import sys

S = sys.stdin.readline().rstrip()
lst = []
i = 0
while i != len(S):
    lst.append(S[i:])
    i += 1
a = sorted(lst)
for i in a:
    print(i)