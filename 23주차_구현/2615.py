import sys
input = sys.stdin.readline

board = [list(map(int, input().split())) for _ in range (19)]
# visit = [[0, 0, 0] * 19 for _ in range (19)]
direction = [(1, 0), (0, 1), (1, 1), (-1, 1)]

# for i in range (19) :
#     for j in range (19) :
#         if i == 0 or j == 0 and map[i][j] != 0 :
#             score[i][j][0], score[i][j][0], score[i][j][0] 
    
def check_5(player, x, y, dx, dy, visit) :
    score = 1
    while True :
        x += dx
        y += dy
        if not(0 <= x <= 18 and 0 <= y <= 18) or board[x][y] != player :
            break
        visit[x][y] = 1
        score += 1
    if score == 5 :
        return True
    else : 
        return False

for dx, dy in direction :
    visit = [[0] * 19 for _ in range (19)]
    r = (18, 3, -1) if dx == -1 else (0, 19 - dx * 4, 1)
    for i in range (r[0], r[1], r[2]) :
        for j in range (19 - dy * 4) :
            if visit[i][j] == 0 and board[i][j] != 0:
                if check_5(board[i][j], i, j, dx, dy, visit) :
                    print(board[i][j])
                    print(i+1, j+1)
                    exit(0)
print(0)