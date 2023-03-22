import sys
input = sys.stdin.readline
from collections import deque

r, c = map(int, input().split())
map = [list(input().strip()) for _ in range (r)]
dp = [[-1 for _ in range (c)] for _ in range (r)] 

d = [(1, 0), (-1, 0), (0, 1), (0, -1)]

jihun = []
fire = deque()
for i in range (r) :
    for j in range (c) :
        if map[i][j] == 'J' :
            jihun = [i, j]
        elif map[i][j] == 'F' :
            fire.append([i, j])  

def BFS(jihun, fire, m) :
    l = len(fire)
    for j in range (l) :
        f = fire.popleft()
        for i in range(4) :
            nf = [f[0] + d[i][0], f[1] + d[i][1]]
            if 0 <= nf[0] < r and 0 <= nf[1] < c :
                if map[nf[0]][nf[1]] != '#' and map[nf[0]][nf[1]] != 'F' :
                    map[nf[0]][nf[1]] = 'F'
                    fire.append([nf[0], nf[1]])
    for i in range(4) :
        nj = [jihun[0] + d[i][0], jihun[1] + d[i][1]]
        if 0 <= nj[0] < r and 0 <= nj[1] < c :
            if map[nj[0]][nj[1]] != '#' and map[nj[0]][nj[1]] != 'F' and dp[nj[0]][nj[1]] == -1:
                # # map[nj[0]][nj[1]] == 'J' # comment 
                # print(map)
                # print("jihun", nj[0], nj[1])
                dp[nj[0]][nj[1]] = m + 1
                BFS([nj[0], nj[1]], fire, m + 1)

dp[jihun[0]][jihun[1]] = 0
BFS(jihun, fire, 0)

result = -1
# print(dp)
for i in range (r) :
    for j in range (c) :
        if i == 0 or j == 0 or i == r-1 or j == c-1 :
            if dp[i][j] != -1 :
                result = dp[i][j] if result == -1 else min(result, dp[i][j])

if result == -1 :
    print("IMPOSSIBLE")
else :
    # print(map)
    print(result + 1)


import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
graph = []

for i in range(n):
    graph.append(list(input().rstrip()))
    if 'J' in graph[i]:
        q = deque([(0, i, graph[i].index('J'))])

for i in range(n):
    for j in range(m):
        if graph[i][j] == 'F':
            q.append((-1, i, j))
            

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
ans = 'IMPOSSIBLE'


while q:
    time, x, y = q.popleft()
    
    if time > -1 and graph[x][y] != 'F' and (x == 0 or y == 0 or x == n - 1 or y == m - 1):
        ans = time + 1
        break

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] != '#':

            if time > -1 and graph[nx][ny] == '.':
                graph[nx][ny] = '_'
                q.append((time + 1, nx, ny))
                
            elif time == -1 and graph[nx][ny] != 'F':
                graph[nx][ny] = 'F'
                q.append((-1, nx, ny))
                

print(ans)