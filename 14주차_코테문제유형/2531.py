import sys
input = sys.stdin.readline

N, d, k, c = map(int, input().split())
list = [int(input()) for i in range (N)]
max_cnt = 0

for i in range (N) :
    event_list = list[i:i+k] if i + k < N else list[i:i+k] + list[:(i + k) - N]
    event_list = set(event_list + [c])
    cnt = len(event_list)
    if cnt == k + 1 :
        max_cnt = k + 1
        break
    max_cnt = max(cnt, max_cnt)

print(max_cnt)

# import sys
# input = sys.stdin.readline

# n, d, k, c = map(int, input().split())
# su_lis = []
# shi = [0]*(d+1)
# shi[c] = 1
# for i in range(n):
#   sushi = int(input())
#   su_lis.append(sushi)

# sushi_kind = 1
# for i in range(k):
#   num = su_lis[i]
#   if shi[num] == 0:
#     sushi_kind += 1

#   shi[num] += 1

# l = 0
# r = k
# answer = sushi_kind
# while True:
#   left_idx = l % n
#   right_idx = r % n
#   left_sushi = su_lis[left_idx]
#   right_sushi = su_lis[right_idx]
  
#   if shi[left_sushi] == 1:
#     sushi_kind -= 1
#   shi[left_sushi] -= 1

#   if shi[right_sushi] == 0:
#     sushi_kind += 1
#   shi[right_sushi] += 1

#   answer = max(answer, sushi_kind)

#   l += 1
#   r += 1
#   if l > n:
#     break
# print(answer)


# 반례
# 8 30 4 30
# 7
# 7
# 3
# 7
# 7
# 8
# 7
# 7
