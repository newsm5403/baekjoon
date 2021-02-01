N = int(input())
i = 0
anw = 1
count = 0
while i != N:
    i += 1
    anw = anw * i
anw = str(anw)
for i in reversed(anw):
    if i == '0':
        count += 1
    else:
        break
print(count)