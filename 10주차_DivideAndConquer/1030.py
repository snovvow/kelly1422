import sys
input = sys.stdin.readline

def check_black(l, x, y):
    center = l//N
    if l == 1:
        return 0
    if center * (N-K)//2 <= x < center * (N+K)//2 and center * (N-K)//2 <= y < center * (N+K)//2:
        return 1
    x %= center
    y %= center
    return check_black(l//N, x, y)
s, N, K, R1, R2, C1, C2 = map(int, input().split())
len = N ** s # 한 변의 길이


for i in range(R1, R2+1):
    for j in range(C1, C2+1):
        print(check_black(len, i, j), end = "")
    print()