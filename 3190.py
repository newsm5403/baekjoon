from collections import deque

# 방향 결정 함수
def change_dir(dir, ch):
    if ch == "L":
        dir = (dir-1) % 4
    else:
        dir = (dir+1) % 4
    return dir

N = int(input())
K = int(input())
mapping = [[0] * N for _ in range(N)]
lane = deque()
visited = deque([[0,0]])
mapping[0][0] = 2
x = y = time = 0
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]
dir = 1

# apple 위치 저장
for _ in range(K):
    apple_y, apple_x = list(map(int, input().split()))
    mapping[apple_y-1][apple_x-1] = 1

# L 저장
L = int(input())
for i in range(L):
    lane.append(list(input().split()))
    lane[i][0] = int(lane[i][0])

while True:
    time += 1
    # 현재 위치 계산
    x, y  = x + dx[dir], y + dy[dir]

    if 0 <= x < N and 0 <= y < N and mapping[y][x] != 2:
        if mapping[y][x] != 1:
            visited_y, visited_x = visited.popleft()
            mapping[visited_y][visited_x] = 0
            
        mapping[y][x] = 2
        visited.append([y, x])

        # 방향 전환 루프
        for i in range(len(lane)):
            if lane[i][0] == time:
                dir = change_dir(dir, lane[i][1])
                lane.popleft()
                break
    else:
        break
print(time)
