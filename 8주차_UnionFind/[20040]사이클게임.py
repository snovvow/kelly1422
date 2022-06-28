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
            
n, m = map(int, input().split())
parent = [i for i in range(n)]
edges = [list(map(int, input().split())) for _ in range(m)]

for idx, info in enumerate(edges) :
    if find(info[0]) != find(info[1]) :
        union(info[0], info[1])
    else :
        print(idx+1)
        break
else:
    print(0)

