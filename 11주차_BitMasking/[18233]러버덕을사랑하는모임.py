import sys
input = sys.stdin.readline
from itertools import combinations

N, P, E = map(int, input().split())
people = [list(map(int, input().split())) for _ in range (N)]
n = [i for i in range (N)]
comb = list(combinations(n, P))
result = [0] * N

flag = 0
for selected in comb :
    minimum = 0
    maximum = 0
    for i in selected :
        minimum += people[i][0]
        maximum += people[i][1]
    if minimum <= E <= maximum :
        flag = 1
        left = E - minimum
        for i in selected :
            result[i] += people[i][0]
            if left > 0 :
                if people[i][1] - people[i][0] >= left :
                    result[i] += left
                    left = 0
                else :
                    result[i] += people[i][1] - people[i][0]
                    left -= (people[i][1] - people[i][0])
        for i in range (N - 1) :
            print(result[i], end=" ")
        print(result[-1])
        break

if flag == 0 :
    print(-1)




