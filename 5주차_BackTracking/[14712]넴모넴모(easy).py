import sys
input = sys.stdin.readline

def check(r, c):
    if board[r-1][c-1] and board[r][c-1] and board[r-1][c]:
        return False
    return True

N, M = map(int, input().split())
board = [[0]*M for _ in range(N)]
ans = 0
def dfs(x, y):
    global ans
    flag = 0
    
    # 대각선위, 위, 왼을 확인 -> 네모 없 : 여기에 네모를 놔도 완성되는 사각형 x -> ans++ 네모 놓고 재귀 진행할 플래그 1
    if x == 0 or y == 0 or check(x, y):
        ans += 1
        flag = 1
    nx, ny = x, y
    if y == M - 1 and x == N - 1 :
        return
    if y == M - 1 :
        nx += 1
        ny = 0
    else:
        ny += 1
    dfs(nx, ny) # 사각형 놓기전에 다음 위치에 사각형 놓기
    if flag: # 현위치에 사각형 놓을 수 있으면 채우고 재귀
        board[x][y] = 1
        dfs(nx, ny)
        board[x][y] = 0

    return

dfs(0, 0)

print(ans + 1)