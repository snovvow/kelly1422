# import sys
# input = sys.stdin.readline

# N, M = map(int, input().split())
# board = ([[0] * (M + 1)]) + [[0] + list(map(int, input().split())) for _ in range (N)]

# for i in range (1, N + 1) :
#     for j in range (1, M + 1) :
#         board[i][j] += (board[i - 1][j] + board[i][j - 1] - board[i - 1][j - 1])

# K = int(input())
# for i in range (K) :
#     r1, c1, r2, c2 = map(int, input().split())
#     sum = board[r2][c2] - board[r1 - 1][c2] - board[r2][c1 - 1] + board[r1 - 1][c1 -1]
#     print(sum)

import sys
input = sys.stdin.readline
mis = lambda: map(int, input().split())
from itertools import accumulate

H, W = mis()
arr = [list(mis()) for i in range(H)]
print(arr)
dp = [[0] * (W+1)]
dp.append([0] + list(accumulate(arr[0])))
print(dp)
for i in range(1, H):
    l = list(accumulate(arr[i]))
    for j in range(W):
        l[j] += dp[-1][j+1]

    dp.append([0] + [x for x in l])
print(dp)

# Q = int(input())
# for _ in range(Q):
#     y, x, yy, xx = mis()
#     print(dp[yy][xx] - dp[y-1][xx] - dp[yy][x-1] + dp[y-1][x-1])