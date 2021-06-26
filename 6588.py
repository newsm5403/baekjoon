def prime_num():
    prime_number = [False, False] + [True] * 10000002
    for i in range(2, 1000002):
        if prime_number[i] == True:
            for k in range(2*i, 1000002, i):
                prime_number[k] = False
    return prime_number

def get_anw(n, lst):
    a = 0
    b = n
    while a <= n//2:
        if lst[a] and lst[b]:
            return print("{} = {} + {}".format(str(n), str(a), str(b)))
        else:
            a += 1
            b -= 1
    print("Goldbach's conjecture is wrong.")

lst = prime_num()
while True:
    n = int(input())
    if n == 0:
        break
    get_anw(n, lst)