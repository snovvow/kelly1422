import sys
input = sys.stdin.readline

str1, str2 = input().strip(), input().strip()
cache = [0] * len(str2)

for i in range(len(str1)):
    cnt = 0
    for j in range(len(str2)):
        if cnt < cache[j]:
            cnt = cache[j]
        elif str1[i] == str2[j]:
            cache[j] = cnt + 1

print(max(cache))