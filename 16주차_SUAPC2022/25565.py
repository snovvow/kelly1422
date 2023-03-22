import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
map = [list(map(int, input().split())) for _ in range (N)]

seed = 0
for i in range (N) :
    for j in range (M) :
        if map[i][j] == 1 :
            seed += 1

x = 0
if seed == 2 * K :
    print(0)
elif K == 1 :
    for i in range (N) :
        for j in range (M) :
            if map[i][j] == 1 :
                print(1)
                print(i, " ", j)
elif seed == 2 * K - 1 :
    for i in range (N) :
        for j in range (M) :
            if map[i][j] == 1 and map[i+1][j] == 1 and map[i][j+1] == 1:
                x = 1
                print(1)
                print(i, " ", j)
else :
    start = []
    dir = []
    cnt = 0
    for i in range (N) :
        for j in range (M) :
            if map[i][j] == 1 :
                start = [i, j]
                if map[i+1][j] == 1 :
                    dir = [1, 0]
                else :
                    dir = [0, 1]

                while [i][j] == 1 :
                    i += dir[0]
                    j += dir[1]
                    cnt += 1
                break
        if cnt != 0 :
            break

    print((2 * K) - cnt)
    for i in range ((2 * K) - cnt) :

        start[]
