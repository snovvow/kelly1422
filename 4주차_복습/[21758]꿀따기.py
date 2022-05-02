import sys
input = sys.stdin.readline

N = int(input())
dp = list(map(int, input().split()))
sum = [0 for i in range (N)]
sum[0] = dp[0]
for i in range (1, N) :
    sum[i] = dp[i] + sum[i - 1]

honey = 0
for i in range (N) :
    if i == 0 :
        for j in range (1, N - 1) :
            honey = max(sum[N-2] - dp[j] + sum[j-1], honey)
    elif 0 < i < N - 1 :
        honey = max( sum[N-2] - dp[0] + dp[i] , honey)
    else :
        for j in range (1, N - 1) :
            honey = max(sum[N-1] * 2 - dp[j] - sum[j] - dp[0], honey)
print(honey)