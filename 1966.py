import sys

T = int(sys.stdin.readline())
for i in range(T):
    stk = []
    cnt = 0
    N, M = list(map(int, sys.stdin.readline().split()))
    importance = list(map(int, sys.stdin.readline().splite()))
    lst = importance
    maxtmp = max(importance)
    if N == 1:
        print(1)
        continue
    else: # 원본에서 빼낼 때 원본의 index값도 같이 넘겨줘야 함
        i = 0
        while True:
            if importance[i] == maxtmp:
                stk.append(importance[i])
                cnt += 1   
                if i == M:
                    print(cnt)
                    break
            i += 1
            maxtmp = max(importance)