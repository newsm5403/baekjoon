import sys
# 먼저 팰린드롬을 검색한 후에 소수를 구해야함
# 팰린드롬은 10000000을 초과하면 없음
def prime_number(B):
    C = int(B ** 0.5)
    for i in range(2, C+1):
        if B % i == 0:
            return False
    return True

def palindrome(i):
    if i == i[::-1]:
        return True

A, B = map(int, input().split())
if B > 10000000:
    B = 10000000
palinlst = [i for i in range(A, B+1) if palindrome(str(i))]
primelst = [i for i in palinlst if prime_number(i)]
for i in primelst:
    print(i)
print(-1)

