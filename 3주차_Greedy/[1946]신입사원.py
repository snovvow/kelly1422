import sys
input = sys.stdin.readline

def ans(T) :
    for _ in range (T) :
        N = int(input())
        arr = [0 for _ in range (N + 1)]
        for _ in range (N) :
            a, b = (map(int, input().split()))
            arr[a] = b
        new = 1
        min = arr[1]
        for i in arr[2:] :
            if min > i :
                min = i
                new += 1
        print(new)

T = int(input())
ans(T)