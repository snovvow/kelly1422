import collections as C, itertools as I, sys
input = sys.stdin.readline

n = int(input())
d = C.defaultdict(int) # 딕셔너리와 비슷, 초기값은 괄호안에 써준 자료형의 기본값 -> 값을 지정하지 않은 키는 그 값이 0으로 저장됨

for i in range(n):
    x, y = map(int, input().split())
    d[x] += 1
    d[y] -= 1
print(max(I.accumulate(d[i]for i in sorted(d))))


# ------------------------------------------------------------------
# import sys
# minf = -float('inf')
# n = int(sys.stdin.readline())
# if n == 1:
#     print(1)
#     exit()
# arr1 = [minf]
# arr2 = [minf]
# k = n << 1
# for i in range(n):
#     x, y = map(int, sys.stdin.readline().split())
#     arr1.append(x)
#     arr2.append(y)
# arr1.sort()
# arr2.sort()
# print(arr1)
# print(arr2)

# ans = cnt = 0
# s1 = s2 = 1

# if arr1[0] < n :
#     print("-inf < n")
# for i in range(1, k + 1):
#     if s1 < n:
#         if arr1[s1] < arr2[s2]:
#             cnt += 1
#             s1 += 1
#         else:
#             cnt -= 1
#             s2 += 1
#     else:
#         cnt -= 1
#     ans = max(ans, cnt)
# print(ans)

# ------------------------------------------------------------------
# 시간초과
# import itertools as I, sys
# input = sys.stdin.readline

# n = int(input())
# point = []

# for i in range(n):
#     start, end = map(int, input().split())
#     point.append([start, 1])
#     point.append([end, -1])

# point.sort()
# print(max(I.accumulate(point[i][1] for i in range (n * 2))))
#------------------------------------------------------------------

