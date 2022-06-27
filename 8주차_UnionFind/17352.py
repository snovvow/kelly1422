import sys
input = sys.stdin.readline

def find(x):
    if parent[x] != x:
        return find(parent[x])
    return parent[x]

def union(a, b):
    a = find(a)
    b = find(b)

    if a != b :
        if a < b:
            parent[b] = a
        else :
            parent[a] = b

N = int(input())
parent = {i: i for i in range(1, N + 1)}

for _ in range(N - 2):
    a, b = map(int, input().split())
    union(a, b)

group1 = find(1)
for i in range(2, N + 1):
    if group1 != find(i):
        print(group1, i)
        break

    