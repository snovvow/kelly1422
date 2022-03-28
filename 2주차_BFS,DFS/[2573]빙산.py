import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
grid = []
for _ in range(N):
    grid.append(list(map(int, sys.stdin.readline().split())))

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
def bfs(i, j):
    visited = [[False] * M for _ in range(N)]
    visited[i][j] = True
    q = deque([[i, j]])
    ice_cnt = 1
    zeros = []
    while q:
        x, y = q.popleft()
        zero_cnt = 0
        for i in range(4):
            nx, ny = x+dx[i], y +dy[i]
            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
                if grid[nx][ny] != 0:
                    q.append([nx, ny])
                    visited[nx][ny] = True
                    ice_cnt += 1
                else:
                    zero_cnt += 1
        if zero_cnt:
            zeros.append([x, y, zero_cnt])
    return ice_cnt, zeros

ans = 0
ice = []
for i in range(N):
    for j in range(M):
        if grid[i][j] != 0:
            ice.append([i, j])
while True:
    if not ice:
        ans = 0
        break
    cnt, zeros = bfs(ice[0][0], ice[0][1])
    if cnt != len(ice):
        break
    for i, j, c in zeros:
        grid[i][j] -= c
        if grid[i][j] <= 0:
            grid[i][j] = 0
            ice.remove([i, j])
    ans += 1
print(ans)