import sys
input = sys.stdin.readline

n = int(input())
w = list(map(int, input().split()))
w.sort()

target = 1
for x in w :
    if x > target :
        break
    target += x
print(target)