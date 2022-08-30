import sys
input = sys.stdin.readline
from itertools import accumulate

N, K, B = map(int, input().split())
wrong = [int(input()) for _ in range (B)]
traffic_lights = [0] * N
for i in wrong :
    traffic_lights[i - 1] = 1
accumulated = list(accumulate(traffic_lights))

mini = 0
for i in range (N - K + 1) :
    num = accumulated[i + K - 1]
    if i == 0 :
        mini = num
    else :
        num -= accumulated[i - 1]
        mini = min(num, mini)

print(mini)

