# import sys
# input = sys.stdin.readline

# N, S = map(int, input().split())
# num = list(map(int, input().split()))
# dp = [0] * N
# t = -1

# for i in range (N) :
#     for j in range (0, N - i) :
#         dp[j] += num[j + i]
#         if dp[j] == S :
#             t = i
#             break
#     if t != -1 :
#         print(t + 1)
#         break

# if t == -1 :
#     print(0)

import sys
input = sys.stdin.readline

N, S = map(int, input().split())
num = list(map(int, input().split()))

sum = num[0]
i, j = 0, 0
ans = 100001

while True : 
    if sum >= S :
        ans = min(ans, j - i + 1)
        sum -= num[i]
        i += 1
    else :
        j += 1
        if j == N :
            break
        sum += num[j]

print(0) if ans == 100001 else print(ans)
