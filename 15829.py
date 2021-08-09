import sys
L = int(sys.stdin.readline())
lst = sys.stdin.readline()
hash = 0
for i in range(len(lst)-1):
    hash += (ord(lst[i]) - 96) * pow(31, i)
print(hash % 1234567891)