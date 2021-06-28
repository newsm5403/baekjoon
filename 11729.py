def moveHanoi(fromP, tempP, toP, n):
    global lst
    if n == 1:
        lst.append([fromP, toP])
    else:
        moveHanoi(fromP, toP, tempP, n-1)
        lst.append([fromP, toP])
        moveHanoi(tempP, fromP, toP, n-1)

n = int(input())
lst = []
moveHanoi('1', '2', '3', n)
print(len(lst))
for a, b in lst:
    print(a, b, sep=" ")