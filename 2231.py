import sys

N = sys.stdin.readline().rstrip()
i = N
anw = []
while i != '1':
    tmp = int(i)
    for j in i:
        tmp = tmp + int(j)
    if tmp == int(N):
        anw.append(int(i))
    i = str(int(i) - 1)
if len(anw) == 0:
    print(0)
else:
    print(min(anw))