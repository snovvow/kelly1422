import sys
input = sys.stdin. readline

T = int(input())

for i in range (T) :
    N = int(input())
    nums = list(map(int, input().split()))
    value = 0
    max = 0
    for i in range(N-1, -1, -1):
        if(nums[i] > max):
            max = nums[i]
        else:
            value += max - nums[i]
    print(value)
