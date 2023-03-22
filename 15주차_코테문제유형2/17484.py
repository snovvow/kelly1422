import sys
input = sys.stdin. readline
INF = float('inf')

N, M = map(int, input().split())
cost = [list(map(int, input().split())) for _ in range (N)]

dp = [[[INF] * 3 for _ in range (M)] for _ in range (N)]

# 0 : 1,1 이동      1 : 0,1 이동      2: -1,1 이동
for i in range (N) :
    for j in range (M) :
        if i == 0 :
            for r in range (3) :
                dp[i][j][r] = cost[i][j]
            continue
        if j != 0 :
            dp[i][j][0] = min(dp[i-1][j-1][1], dp[i-1][j-1][2]) + cost[i][j]
        if j != M-1 :
            dp[i][j][2] = min(dp[i-1][j+1][0], dp[i-1][j+1][1]) + cost[i][j]
        dp[i][j][1] = min(dp[i-1][j][0], dp[i-1][j][2]) + cost[i][j]

print(min(map(min, dp[N-1])))
