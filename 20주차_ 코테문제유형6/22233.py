import sys
input = sys.stdin.readline

# 집합을 이용한 (차집합) 풀이
n, m = map(int, input().split())
memo = set()

for _ in range (n):
    memo.add(input().rstrip())

for _ in range(m) :
    blog = input().rstrip()
    words = set(blog.split(','))
    memo -= words
    print(len(memo))

# 딕셔너리를 이용한 풀이
# n, m = map(int, input().split())
# memo = dict()
# for _ in range(n) :
#     memo[input().rstrip()] = 1
    
# res = n
# for _ in range(m) :
#     blog = sorted(input().rstrip().split(','))
    
#     for word in blog :
#         if word in memo.keys() :
#             if memo[word] == 1 :
#                 memo[word] -= 1
#                 res -= 1
#     print(res)
