import sys
sys.setrecursionlimit(1000000)

dx, dy = [0, 0, 1, 1, 1, -1, -1, -1], [1, -1, 0, 1, -1, 0, 1, -1]

while True :
    def DFS(i, j, arr, visited) :
        visited[i][j] = 1
        for a in range (8) :
            nx = i + dx[a]
            ny = j + dy[a]
            if 0 <= nx < h and 0 <= ny < w and visited[nx][ny] == 0 and arr[nx][ny]== 1:
                DFS(nx, ny, arr, visited)
                
    w, h = map(int, input().split())

    if w == 0 and h == 0 :
        break
    
    arr = []
    for i in range(h):
        arr.append(list(map(int, input().split())))
    visited = [[0 for _ in range(w)] for _ in range(h)]

    cnt = 0
    for i in range (h) :
        for j in range (w) :
            if arr[i][j] == 1 and visited[i][j] == 0 :
                cnt += 1
                DFS(i, j, arr, visited)

    print(cnt)

# import sys
# sys.setrecursionlimit(100000000)
# input = sys.stdin.readline

# def dfs(x,y):
#     if x<0 or y<0 or x>=h or y>=w:
#         return False
#     if graph[x][y] == 1:
#         graph[x][y]=0
#         dfs(x-1,y)
#         dfs(x,y-1)
#         dfs(x+1,y)
#         dfs(x,y+1)
#         dfs(x-1, y-1)
#         dfs(x-1, y+1)
#         dfs(x+1, y-1)
#         dfs(x+1, y+1)
#         return True
#     return False
    

# while True:
    
#     w, h = map(int, input().split())
#     if w==h==0 : 
#         break
#     graph = []
#     for i in range(h):
#         graph.append(list(map(int, input().split())))

    
#     res = 0
#     for i in range(h):
#         for j in range(w):
#             if dfs(i, j) ==  True:
#                 res+=1
                
                
#     print(res)
