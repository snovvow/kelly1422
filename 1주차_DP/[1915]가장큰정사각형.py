x, y = map(int, input().split())
board = []
biggest = 0

for i in range (x) :
    board.append(list(map(int, input())))
    for j in range (y) :
        if board[i][j] != 0 and j != 0 and i != 0:
            board[i][j] = min(board[i-1][j], board[i][j-1], board[i-1][j-1]) + 1
        biggest = max(board[i][j], biggest)

print(biggest * biggest)