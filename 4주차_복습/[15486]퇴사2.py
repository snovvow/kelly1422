import sys 
input = sys.stdin.readline 

N = int(input())
dp = [0] * (N + 1)
ans= 0
for today in range(N):
    term, price = map(int, input().split())
    if term + today <= N and dp[today + term] < price + ans:
        dp[today + term] = ans + price
    ans= max(ans, dp[today + 1])
print(ans)