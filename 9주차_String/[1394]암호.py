import sys
input = sys.stdin.readline

str = input().strip()
pwd = input().strip()

str_len = len(str)
pwd_len = len(pwd)

cnt = 0
temp = 1

for i in range (pwd_len - 1, -1, -1) :
    idx = str.find(pwd[i])
    cnt = (cnt + temp * (idx + 1)) % 900528
    temp = temp * str_len % 900528

print(cnt)

# import sys
# input = sys.stdin.readline

# str = input().strip()
# pwd = input().strip()

# str_len = len(str)
# pwd_len = len(pwd)

# cnt = 0

# for i in range (1, pwd_len) :
#     cnt += str_len ** (i)

# for i, a in enumerate(pwd) :
#     cnt += (str.find(a) * (str_len ** (pwd_len - 1 - i)))

# print((cnt + 1) % 900528)