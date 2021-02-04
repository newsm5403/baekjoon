""" S = list(input())
first = None
start = 0
end = 0
razer = 0
anw = 0
i = 0
while i != len(S):
    if S[i] == '(' and S[i+1] == ')':
        if first == None:
            S.pop(i)
            S.pop(i)
            continue
        razer += 1
        i += 2
    elif S[i]== '(':
        if first == None:
            first = i
        start += 1
        i += 1
    elif S[i] == ')':
        end += 1
        if start == end:
            anw += razer + 1
            S.pop(i)
            S.pop(first)
            i = 0
            razer = 0
            first = None
            continue
        i += 1
print(anw)
 답은 맞지만 시간초과 ㅠㅠ""" 
N = input()
f = 0
anw = 0
i = 0
while i != len(N):
    if N[i] == '(':
        if N[i+1] == ')':
            anw += f
            i += 1
        else:
            f += 1
    elif N[i] == ')':
        anw += 1
        f -= 1
    i += 1
print(anw)