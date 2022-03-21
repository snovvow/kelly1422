n, k = map(int, input().split())

dp = [[0 for i in range (k)] for j in range (n)]

for i in range (n) :
    for j in range (k) :
        if (i == 0) :
            dp[i][j] = j + 1
        elif (j == 0) :
            dp[i][j] = 1
        else :
            dp[i][j] = dp[i-1][j] + dp[i][j-1]

print(dp[n-1][k-1] % 1000000000)

# N, K = map(int, input().split())
# 	dp = [0 for _ in range(N+1)]
# 	dp[0] = 1

# 	for i in range(K):
# 		for j in range(1, N+1):
# 			dp[j] = dp[j] + dp[j-1]
	
# 	print(dp[N]%MOD)