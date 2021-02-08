N, B = map(int, input().split())
lst = []
while N != 0:
    b = N % B
    if b > 9:
        lst.insert(0, chr(b+55))
    else:
        lst.insert(0, b)
    N = N // B

print(*lst, sep="")