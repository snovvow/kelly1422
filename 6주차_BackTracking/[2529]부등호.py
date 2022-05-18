import sys
input = sys.stdin.readline

k = int(input())
sign = list(map(str, input().split())) 

def check(i, n) :
    if i == 0:
        return True
    if sign[i - 1] == '<' :
        if num[-1] < n :
            return True
    if sign[i - 1] == '>' :
        if num[-1] > n :
            return True
    return False

def bfs_max(x) :
    global complete_max
    if x == k + 1 :
        print(*num, sep = '')
        complete_max = True
        return
    for i in range(10) :                  # 9 ~ 0 까지 역순으로 
        if i not in num and check(x,i) :
            num.append(i)
            bfs_max(x + 1)
            if complete_max :
                break
            num.pop()

def bfs_min(x) :
    global complete_min
    if x == k + 1 : 
        print(*num, sep = '')
        complete_min = True
        return
    for i in range(9, -1, -1) :              # 9 ~ 0 까지 역순으로
        if i not in num and check(x, i) :
            num.append(i)
            bfs_min(x + 1)
            if complete_min :
                break
            num.pop()

complete_max = False
complete_min = False

num = []
bfs_min(0)
num = []
bfs_max(0)