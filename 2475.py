N = list(map(int, input().split()))
anw = 0
for i in N:
    anw += i*i
print(anw%10)