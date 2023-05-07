import sys
input = sys.stdin.readline

A, B = map(int, input().split())
N, M = map(int, input().split())
robots = []
commands = []
dir = ('N', 'E', 'S', 'W')
f_dir = [(0, 1), (1, 0), (0, -1), (-1, 0)]

map = [[0] * (B+1) for _ in range (A+1)]

for i in range (N) :
    x, y, d = input().split()
    robots.append([int(x), int(y), d])
    map[int(x)][int(y)] = len(robots)

for i in range (M) :
    r, c, n = input().split()
    commands.append([int(r), c, int(n)])  

for command in commands :
    if command[1] == 'F' :
        robot = robots[command[0]-1]
        d = f_dir[dir.index(robot[2])]
        for i in range (command[2]) :
            x, y = robot[0], robot[1]
            map[x][y] = 0
            x += d[0]
            y += d[1]
            if not(1 <= x <= A and 1 <= y <= B) :
                print('Robot', command[0], 'crashes into the wall')
                exit(0)
            else :
                if map[x][y] != 0 :
                    print('Robot', command[0], 'crashes into robot', map[x][y])
                    exit(0)
                else :
                    robot[0], robot[1] = x, y 
                    map[x][y] = command[0]

    else :
        n = command[2] if command[1] == 'R' else -command[2]
        robots[command[0]-1][2] = dir[(dir.index(robots[command[0]-1][2]) + n) % 4]

print('OK')
