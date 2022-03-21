n = int(input())

stairs = [0 for i in range (n + 1)]
dp = [0 for i in range (n + 1)]

for i in range (1, n + 1) :
    stairs[i] = int(input())
    if i == 1 :
        dp[1] = stairs[1]
    elif i == 2 :
        dp[2] = stairs[2] + stairs[1]
    else :
        dp[i] = stairs[i] + max(stairs[i-1] + dp[i -3], dp[i - 2])

print(dp[n])