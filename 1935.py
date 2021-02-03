''' import sys

N = int(sys.stdin.readline().rstrip())
M = list(sys.stdin.readline().rstrip())
lst = list(float(input()) for i in range(N)) # 받을 때 float 형으로 받기
stk = []
i = 0
while i != len(M):
    if 'A' <= M[i] <= 'Z': # 알파벳 index 최신화
        idx = len(stk)
    if not 'A' <= M[i] <= 'Z': # 알파벳이 아닌경우 stk에 추가한 뒤 M에서 삭제
        stk.insert(idx, M[i])
        M.pop(i)
        i -= 1
    i += 1
for i in range(len(M)): # M에 있는 알파벳을 숫자로 변환
    M[i] = lst[ord(M[i])-65]

for i in range(len(stk)): # stk에 있는 부호들을 M에 삽입
    M.insert(2*i+1, stk[i])
M = ''.join(str(e) for e in M) # M을 string형으로 변환
print(M)
print("%.2f" % eval(M)) # eval() 함수로 계산한 뒤 소수점 둘째자리까지 반환 
------------------------첫번째 코드(틀렸습니다 why???? 아직 모르겠음...)'''
import sys
N = int(sys.stdin.readline().rstrip())
M = list(sys.stdin.readline().rstrip())
lst = list(float(input()) for i in range(N)) # 받을 때 float 형으로 받기
stk = []
for i in range(len(M)):
    if 'A' <= M[i] <= 'Z':
        stk.append(lst[ord(M[i])-65])
    else:
        b = stk.pop()
        a = stk.pop()
        if M[i] == '+':
            stk.append(a+b)
        elif M[i] == '-':
            stk.append(a-b)
        elif M[i] == '*':
            stk.append(a*b)
        elif M[i] == '/':
            stk.append(a/b)
print('%.2f' % stk[0])