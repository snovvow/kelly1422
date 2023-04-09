import sys
from itertools import combinations 
input = sys.stdin.readline

N, M = map(int, input().split())
city = [list(map(int, input().split())) for _ in range (N)]

homes = []
chickens = []

for i in range (N) :
    for j in range (N) :
        if city[i][j] == 1 :
            homes.append((i, j))
        elif city[i][j] == 2 :
            chickens.append((i, j))


def get_distance(homes, chickens) :
    city_distance = 0
    for home in homes :
        distance = 1000
        for chicken in chickens :
            distance = min(distance, abs(home[0] - chicken[0]) + abs(home[1] - chicken[1]))
        city_distance += distance
    return city_distance

result = 10000
for comb in combinations(chickens, M) :
    result = min(result, get_distance(homes, comb))
    
print(result)