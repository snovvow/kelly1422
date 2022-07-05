# import sys
# input = sys.stdin.readline

# T = int(input())

# for _ in range (T) :
#     sign = input().strip()
#     idx = 0
#     if sign[0] == "1" :
#         print("1: 1")
#         idx = 1

#     flag = 1

#     sign_len = len(sign)

#     while idx < sign_len :
#         print("start : ", idx, len(sign))
#         if idx < sign_len - 2 and sign[idx] == "0" and sign[idx + 1] == "0" :
#             print("00 step")
#             idx += 2
#             while idx < sign_len and sign[idx] == "0" :
#                 idx += 1
#             if idx < sign_len and sign[idx] == "1" :
#                 while idx < sign_len and sign[idx] == "1" :
#                     idx += 1
#             else :
#                 flag = 0
#                 break
        
#         elif idx < sign_len - 1 and sign[idx] == "0" and sign[idx + 1] == "1" :
#             print("01 step")
#             idx += 2
#             if idx < sign_len and sign[idx] == "1" :
#                 idx += 1
#         else : 
#             print("else")
#             flag = 0
#             break

#     if flag == 0 :
#         print("NO")
#     else :
#         print("YES")

import re
import sys
input = sys.stdin.readline
 
T = int(input())
results = []
 
for _ in range(T):
    sign = input().strip()
    expression = re.compile('(100+1+|01)+')
    included = expression.fullmatch(sign)
    if included :
        print("YES")
    else :
        print("NO")