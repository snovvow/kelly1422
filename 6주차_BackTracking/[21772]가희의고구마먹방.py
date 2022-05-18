import sys
input = sys.stdin.readline

N, M, T = map(int, input().split())
map = [list(input()) for i in range (N)]

dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]

for i in range (N) :
    for j in range (M) :
        if map[i][j] == 'G' :
            sx = i
            sy = j
            map[i][j] = '.'

maxsize = 0

def bfs(x, y, t, size) :
    global maxsize
    if t == T :
        return 
    else :
        for i in range (4) :
            x2, y2 = dx[i] + x, dy[i] + y
            if 0 <= x2 < N and 0 <= y2 < M :
                if map[x2][y2] == 'S' :
                    map[x2][y2] = '.'
                    maxsize = max(size + 1, maxsize)
                    bfs(x2, y2, t + 1, size + 1)
                    map[x2][y2] = 'S'
                elif map[x2][y2] == '.':
                    bfs(x2, y2, t + 1, size)

bfs(sx, sy, 0, 0)
print(maxsize)