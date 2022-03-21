N, M = map(int, input().split())

candy = []
dp = [[0 for i in range(M)] for j in range(N)]
# dp = [[0] * m for _ in range(n)]

for i in range (N) :
    candy.append(list(map(int, input().split())))
dp[0][0] = candy[0][0]

def next(x, y) :
    if x < N - 1 :
        dp[x+1][y] = max(dp[x+1][y], dp[x][y] + candy[x+1][y])
    if y < M - 1 :
        dp[x][y+1] = max(dp[x][y+1], dp[x][y] + candy[x][y+1])
    if x < N - 1 and y < M - 1 :
        dp[x+1][y+1] = max(dp[x+1][y+1], dp[x][y] + candy[x+1][y+1])

for i in range (N) :
    for j in range (M) :
        next(i, j)

print(dp[N-1][M-1])