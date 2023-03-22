import sys
input = sys.stdin.readline
from collections import deque

# n, k = map(int, input().split())
# belt = deque(list(map(int, input().split())))
# robot = deque([0]*n)
# res = 0

# while 1:
#     belt.rotate(1)
#     robot.rotate(1)
#     robot[-1]=0 #로봇이 내려가는 부분이니 0
#     if sum(robot): #로봇이 존재하면
#         for i in range(n-2, -1, -1): #로봇 내려가는 부분 인덱스 i-1 이므로 그 전인 i-2부터
#             if robot[i] == 1 and robot[i+1] == 0 and belt[i+1]>=1:
#                 robot[i+1] = 1
#                 robot[i] = 0
#                 belt[i+1] -= 1
#         robot[-1]=0
#     if robot[0] == 0 and belt[0]>=1:
#         robot[0] = 1
#         belt[0] -= 1
#     res += 1
#     if belt.count(0) >= k:
#         break
                
# print(res)

n, k = map(int, input().split())
belt = deque(map(int, input().split()))
robots = deque([False] * 2 * n)
up, down = 0, n - 1

step = 0
while k > 0:
    step += 1

    belt.rotate(1)
    robots.rotate(1)
    robots[n - 1] = False

    if any(robots):
        for i in range(n - 1, 0, -1):
            if belt[i] > 0 and not robots[i] and robots[i - 1]:
                robots[i], robots[i - 1] = True, False
                belt[i] -= 1
                if not belt[i]:
                    k -= 1
                if i == n - 1:
                    robots[i] = False

    if belt[0] > 0:
        robots[0] = True
        belt[0] -= 1
        if not belt[0]:
            k -= 1

print(step)