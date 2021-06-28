T = int(input())
for i in range(T):
    data = 1
    a,b = map(int, input().split())
    for j in range(b):
        data = data * a % 10
    if data % 10 == 0:
        print(10)
    else:
        print(data)