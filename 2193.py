N = int(input())
fibo = [0, 1]
for i in range(N):
    fibo.append(fibo[0] + fibo[1])
    fibo.pop(0)
print(fibo[0])