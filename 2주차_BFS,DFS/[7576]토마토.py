from collections import deque

m, n = map(int, input().split())

tomato = [list(map(int, input().split())) for i in range (n)]
q = deque([])
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]

for i in range (n) :
    for j in range (m) :
        if tomato[i][j] == 1 :
            q.append([i, j])

cnt = 0

def bfs() :
    while q:
        x, y = q.popleft()
        for i in range (4) :
            x2, y2 = dx[i] + x, dy[i] + y
            if 0 <= x2 < n and 0 <= y2 < m and tomato[x2][y2] == 0 :
                tomato[x2][y2] = tomato[x][y] + 1
                q.append([x2, y2])

bfs()

for i in range (n) :
    for j in range (m) :
        if tomato[i][j] == 0 :
            print("-1")
            exit(0)
        cnt = max(cnt, tomato[i][j])
        
print(cnt - 1)