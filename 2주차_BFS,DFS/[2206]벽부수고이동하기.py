from collections import deque
import sys

N, M = map(int, input().split())

arr = []
for i in range (N) :
    arr.append(list(map(int, sys.stdin.readline().strip())))
visited = [[[0] * 2 for _ in range (M)] for _ in range (N)]
visited[0][0][0] = 1

dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]

def BFS(x, y, z) :
    q = deque()
    q.append((x, y, z))

    while q:
        a, b, c = q.popleft()
        if a == N - 1 and b == M - 1 :
            return visited[a][b][c]
        for i in range (4):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0 <= nx < N and 0 <= ny < M :
                if arr[nx][ny] == 1 and c == 0 :
                    visited[nx][ny][1] = visited[a][b][0] + 1
                    q.append((nx, ny, 1))
                elif arr[nx][ny] == 0 and visited[nx][ny][c] == 0 :
                    visited[nx][ny][c] = visited[a][b][c] + 1
                    q.append((nx, ny, c))
    return -1

print(BFS(0,0,0))