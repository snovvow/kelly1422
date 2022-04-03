import sys
input = sys.stdin.readline
n = int(input())
cow = []
for _ in range (n) :
    cow.append(list(map(int, input().split())))
cow.sort()
arrive = 0
for a, b in cow :
    arrive = max(arrive, a) + b
print(arrive)