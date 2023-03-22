import sys
input = sys.stdin. readline

H, W = map(int, input().split())
block = list(map(int, input().split()))

if sum(block) == 0 :
    print(0)
else :
    while block[0] == 0 :
        block.pop(0)
    while block[-1] == 0 :
        block.pop(1)

    rain = 0
    for i in range (1, len(block) - 1) :
        left_max = max(block[:i])
        right_max = max(block[i+1:])
        min_max = min(left_max, right_max)

        if block[i] < min_max :
            rain += min_max - block[i]

    print(rain)
    
