import sys
input = sys.stdin.readline

N = int(input())
balls = input().rstrip()

colors = []

i = 0
while i < N :
    j = i
    while j < N and balls[j] == balls[i] :
        j += 1
    colors.append([balls[i], j - i])
    i = j

red_right = 0
red_left = 0
blue_right = 0
blue_left = 0

part = len(colors)

for i in range (part - 2, -1, -1) :
    if colors[i][0] == 'R' :
        red_right += colors[i][1]
    else : 
        blue_right += colors[i][1]

for i in range (1, part) :
    if colors[i][0] == 'R' :
        red_left += colors[i][1]
    else : 
        blue_left += colors[i][1]

print(min(red_left, red_right, blue_left, blue_right))