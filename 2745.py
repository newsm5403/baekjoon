N, B = input().split()
B = int(B)
a = 0
for i in range(len(N)):
    if 'A' <= N[i] <= 'Z':
        tmp = ord(N[i]) - 65 + 10
    else:
        tmp = int(N[i])
    if N[i] == '0':
        continue
    else:
        a += pow(B,len(N)-1-i) * tmp
print(a)