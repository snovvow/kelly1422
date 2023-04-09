import sys
input = sys.stdin.readline

T = int(input())
dp = [1, 2, 4, 7, 13]

def by123(n) :
    for i in range (len(dp), n) :
        sum = (dp[i - 1] + dp[i - 2] + dp[i - 3]) % 1000000009
        dp.append(sum)
    print(dp[n-1])

for _ in range(T) :
    n = int(input())
    by123(n)