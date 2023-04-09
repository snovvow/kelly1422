import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())
map = [list(map(int, input().split())) for _ in range (n)]
dp = [[0] * n for _ in range (n)]

direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def DFS(x, y) :
    if dp[x][y] != 0 : 
        return dp[x][y]
    dp[x][y] = 1
    for dx, dy in direction :
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < n and map[x][y] < map[nx][ny] :
                dp[x][y] = max(dp[x][y], 1 + DFS(nx, ny))
    return dp[x][y]

ans = 0
for i in range (n) :
    for j in range (n) :
        DFS(i, j)

print(max(map(max,dp))+1)