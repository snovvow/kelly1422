import sys
input = sys.stdin.readline

n = int(input())
array = []

for i in range (n) :
    str = input().strip()
    array.append(list(str[2:].split()))
array.sort()

same = 0
for i in range (len(array)) :
    same = 0
    if i != 0 :
        for j in range(len(array[i-1]) - 1) :
            if array[i][j] == array[i-1][j] :
                same += 1
            else :
                break
    for j in range(same, len(array[i])) :
        print(j * '--', end='')
        print(array[i][j])
    