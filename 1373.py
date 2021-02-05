''' N = list(input())
stk = []
rest = 3 - len(N) % 3
if rest != 0:
    for i in range(rest):
        N.insert(0, '0')
sentence = len(N) // 3
for i in range(sentence):
    a = int(N[0])*4 + int(N[1])*2 + int(N[2])*1
    stk.append(a)
    N.pop(0)
    N.pop(0)
    N.pop(0)
print(*stk) 시간초과 뜬다. '''
print(oct(int(input(), 2))[2:])