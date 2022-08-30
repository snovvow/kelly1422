import sys
input = sys.stdin.readline

N, r, c = map(int, input().split())

cnt = 0

while N >= 1 :
    if (2 ** (N - 1)) <= r < (2 ** (N)) and (2 ** (N - 1)) <= c < (2 ** (N)):
        r -= (2 ** (N - 1))
        c -= (2 ** (N - 1))
        cnt += ((2 ** (N - 1)) ** 2) * 3
    elif (2 ** (N - 1)) <= r < (2 ** (N)) :
        r -= (2 ** (N - 1))
        cnt += ((2 ** (N - 1)) ** 2) * 2
    elif (2 ** (N - 1)) <= c < (2 ** (N)) :
        c -= (2 ** (N - 1))
        cnt += ((2 ** (N - 1)) ** 2) * 1
    N -= 1
print(cnt)
