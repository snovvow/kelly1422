import sys
input = sys.stdin.readline

R, C, Q = map(int, input().split())
board = [list(map(int, input().split())) for _ in range (R)]

for i in range (R) :
    for j in range (C) :
        if i == 0 and j == 0 :
            continue
        elif i == 0 :
            board[i][j] += board[i][j - 1]
        elif j == 0 :
            board[i][j] += board[i - 1][j]
        else :
            board[i][j] += (board[i - 1][j] + board[i][j - 1] - board[i - 1][j - 1])

for i in range (Q) :
    r1, c1, r2, c2 = map(int, input().split())
    r1 -= 1
    c1 -= 1
    r2 -= 1
    c2 -= 1
    num = (r2 - r1 + 1) * (c2 - c1 + 1)
    sum = board[r2][c2]
    if r1 != 0 :
        sum -= board[r1 - 1][c2]
    if c1 != 0 :
        sum -= board[r2][c1 - 1]
    if r1 != 0 and c1 != 0 :
        sum += board[r1 - 1][c1 -1]
    print(sum // num)

