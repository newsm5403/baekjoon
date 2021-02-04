S = input()
stk = []
anw = []
i = 0
while i != len(S):
    if S[i] == '<':
        while True:
            anw.append(S[i])
            i += 1
            if S[i] == '>':
                anw.append(S[i])
                i += 1
                break
    else:
        while True:
            stk.append(S[i])
            i += 1
            if i == len(S):
                anw.append(''.join(stk[::-1]))
                break
            if S[i] == ' ':
                anw.append(''.join(stk[::-1]))
                anw.append(S[i])
                stk = []
                i += 1
                continue
            if S[i] == '<':
                anw.append(''.join(stk[::-1]))
                stk = []
                break      
print(*anw, sep="")