import sys
input = sys.stdin.readline

N = int(input())
M = int(input())

cities = [0] * (N + 1)
for i in range (1, N + 1) :
    cities[i] = i

def find_root(cities, city) :
    if cities[city] != city:
        return find_root(cities, cities[city])
    return cities[city]

def union_city(cities, cityA, cityB) :
    a = find_root(cities, cityA)
    b = find_root(cities, cityB)
    if a != b :
        if a < b :
            cities[b] = a
        else :
            cities[a] = b

for i in range (1, N + 1) :
    connected = list(map(int, input().split()))
    for j in range (1, N + 1) :
        if connected[j - 1] == 1 :
            union_city(cities, i, j)

route = list(map(int, input().split()))
possible = set([find_root(cities, i) for i in route])

if len(possible) == 1 :
    print("YES")
else :
    print("NO")

