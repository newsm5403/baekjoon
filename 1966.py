import sys

def getmax(lst):
    tmp = []
    for i in lst:
        tmp.append(i[0])
    return max(tmp)

T = int(sys.stdin.readline())
anw = []
for i in range(T):
    N, M = list(map(int, sys.stdin.readline().split()))
    lst = list(map(int, sys.stdin.readline().split()))
    idxlst = []
    cnt = 0
    for i in range(N):
        idxlst.append([lst[i], i])
    
    while True:
        maxtmp = getmax(idxlst)
        if idxlst[0][0] == maxtmp: # max 값과 같으면
            if idxlst[0][1] == M:
                cnt += 1
                anw.append(cnt)
                break
            idxlst.pop(0) # 맨앞 pop first
            cnt += 1 # 뺀 순서 count
        else:
            tmp = idxlst.pop(0) # max 값과 다르면 pop 해서 last in
            idxlst.append(tmp)
   
for i in anw:
    print(i)