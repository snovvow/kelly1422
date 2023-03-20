from collections import deque
import sys
input = sys.stdin.readline

N, L, R = map(int, input().split())

nation = [list(map(int, input().split())) for _ in range (N)]

dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]

def BFS(a, b) :
    q = deque()
    temp = []
    q.append((a, b))
    temp.append((a, b))
    while (q) :
        x, y = q.popleft()
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and visit[nx][ny] == 0 and L <= abs(nation[x][y] - nation[nx][ny]) <= R :
                        visit[nx][ny] = 1
                        q.append((nx, ny))
                        temp.append((nx, ny))
    return temp


cnt = 0
while True:
    visit = [[0] * N for _ in range (N)]
    flag = 0
    for i in range(N) :
        for j in range(N) :
            if visit[i][j] == 0 :
                visit[i][j] = 1
                connect = BFS(i, j)
                if len(connect) > 1 :
                    flag = 1
                    average = sum(nation[x][y] for x, y in connect) // len(connect)
                    for x, y in connect :
                        nation[x][y] = average
    if flag == 0 :
        break
    cnt += 1

print(cnt)