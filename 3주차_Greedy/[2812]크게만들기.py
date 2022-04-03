import sys
input = sys.stdin.readline

N, K = map(int, input().split())
num = input().strip()
result = [num[0]]
for i in num[1:] :
    while K > 0 and result and result[-1] < i :
            result.pop()
            K -= 1
    result.append(i)

if K > 0:
    result = result[:-K]
print("".join(result))
