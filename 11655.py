import sys

S = sys.stdin.readline().rstrip()
for i in S:
    if 65 <= ord(i) <= 90: #대문자
        i = chr(ord(i)+13)
        if ord(i) > 90:
            i = chr(ord(i) % 90 + 64)
        print(i, end="")
    elif 97 <= ord(i) <= 122: #소문자
        i = chr(ord(i)+13)
        if ord(i) > 122:
            i = chr(ord(i) % 122 + 96)
        print(i, end="")
    else:
        print(i, end="")