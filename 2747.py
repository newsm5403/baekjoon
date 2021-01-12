n = int(input())
anw = [0, 1]
for i in range(2, n+1):
    anw.append(anw[i-1] + anw[i-2])
print(anw[-1])