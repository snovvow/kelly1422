import sys
input = sys.stdin.readline


n, k = map(int, input().split())

def dfs(sum, check):
    global cnt
    if sum > n:
        return

    if n == sum:
        cnt += 1
        if cnt == k:
            print(''.join(check)[:-1])
            exit(0)

    for i in range(1, 4):
        check.append(str(i) + '+')
        dfs(sum + i, check)
        check.pop()


cnt = 0
dfs(0, [])
print(-1)



# import sys
# from itertools import permutations
# input = sys.stdin.readline

# n, k = map(int, input().split())
# numarr = []

# for i in range (n // 3 + 1) :
#     for j in range ((n - (i*3)) // 2 + 1) :
#         comb = []
#         for _ in range (i) :
#             comb.append(3)
#         for _ in range (j) :
#             comb.append(2)
#         for _ in range (n - (i*3) - (j*2)) :
#             comb.append(1)
#         numarr.append(comb)

# result = []

# for num in numarr :
#     for per in permutations(num) :
#         result.append(per)

# result = set(result)
# result2 = sorted(result)
# if len(result2) < k :
#     print(-1)
# else :
#     ans = result2[k-1]
#     for i in range (len(ans) - 1) :
#         print(ans[i], end='+')
#     print(ans[-1])
