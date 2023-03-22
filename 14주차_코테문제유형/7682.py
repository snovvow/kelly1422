import sys
input = sys.stdin.readline

def is_over(board, player) :
    for i in range (3) :
        idx = i * 3
        if board[idx] == board[idx + 1] == board[idx + 2] == player :
            return True
    for i in range (3) :
        if board[i] == board[i + 3] == board[i + 6] == player :
            return True
    if board[0] == board[4] == board[8] == player :
        return True
    if board[2] == board[4] == board[6] == player :
        return True
    return False

while True :
    board = input().strip()
    if board == "end" :
        break
    else :
        if board.count('X') == board.count('O') or (board.count('X') == board.count('O') + 1) :
            player = []
            if board.count('X') == board.count('O') + 1 :
                player = ['X', 'O']
            else :
                player = ['O', 'X']
                
            if is_over(board, player[1]) :
                print("invalid")
            elif is_over(board, player[0]) :
                print("valid")
            elif '.' not in board :
                print("valid")
            else :
                print("invalid")
        else :
            print("invalid")