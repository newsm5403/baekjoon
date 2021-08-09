N, M = list(map(int, input().split()))
lst = []
anw = []
for i in range(N):
    lst.append(input())

for i in range(N-7):
    for j in range(M-7):
        cnt_W = 0
        cnt_B = 0
        for k in range(i,i+8): # 8*8 타일 탐색
            for l in range(j,j+8):
                if (k+l) % 2 == 0: # 스타팅
                    if lst[k][l] != "W": # 처음이 W가 아닐경우(처음이 W라고 가정)
                        cnt_W += 1
                    if lst[k][l] != "B": # 처음이 B가 아닐경우(처음이 B라고 가정)
                        cnt_B += 1
                else:
                    if lst[k][l] != "B": # 처음이 W라고 가정했으므로 홀수 타일은 무조건 B가 와야함
                        cnt_W += 1       # 근데 B가 안왔으므로 cnt_W++
                    if lst[k][l] != "W": # 처음이 B라고 가정했으므로 홀수 타일은 무조건 W가 와야함
                        cnt_B += 1       # 근데 W가 안왔으므로 cnt_B++
        anw.append(cnt_W)
        anw.append(cnt_B)
print(min(anw))