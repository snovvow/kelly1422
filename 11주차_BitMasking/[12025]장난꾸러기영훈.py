# import sys
# input = sys.stdin.readline

# if __name__ == "__main__" : 
#     num = list(map(str, input()))
#     num.pop()
#     k = int(input())
#     cnt = (num.count('1') + num.count('6') + num.count('2') + num.count('7'))

#     if k > (2 ** cnt) or k <= 0 :
#         print(-1)
#     else :
#         bit = bin(k - 1)[2:]
#         bit = '0' * (cnt - len(bit)) + bit
#         idx = 0
#         for i in range (len(num)) :
#             if num[i] in '1267' :
#                 if bit[idx] == '0' :
#                     num[i] = '1' if num[i] in '16' else '2'
#                 else :
#                     num[i] = '6' if num[i] in '16' else '7'
#                 idx += 1

        # print(''.join(num))


# 비트연산 사용
num = list(input())
idxs = []
for i in range(len(num)):
    if num[i] in '16':
        num[i] = '1'
        idxs.append(i)
    elif num[i] in '27':
        num[i] = '2'
        idxs.append(i)

k = int(input()) - 1
if 0 <= k < 2 ** len(idxs) :
    ans = list(num)
    for i in range(len(idxs)):
        if k & (2 ** (len(idxs) - 1 - i)):
            num[idxs[i]] = chr(ord(num[idxs[i]]) + 5)
    print(''.join(num))
else:
    print(-1)
