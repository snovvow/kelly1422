import sys
input = sys.stdin.readline

N = int(input())

board = [list(map(int, input().split())) for _ in range (N)]

white = 0
blue = 0

def rec(x, y, n) :
    global white
    global blue
    same = 1
    first = board[x][y]
    for i in range (x, x + n) :
        for j in range (y, y + n) :
            if first != board[i][j] :
                same = 0
                break
    if same == 1 :
        if first == 1 :
            blue += 1
        else : 
            white += 1
    else :
        rec(x, y, n//2)
        rec(x, y + n//2, n//2)
        rec(x + n//2, y, n//2)
        rec(x + n//2, y + n//2, n//2)

rec(0, 0, N)
print(white)
print(blue)
