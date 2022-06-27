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

testcase = int(input())
for i in range (testcase) :
    print("Scenario ", end="")
    print(i + 1, end="")
    print(":")

    user = int(input())
    parent = {n: n for n in range(user)}

    relation = int(input())
    for j in range (relation) :
        a, b = map(int, input().split())
        union(a, b)
    
    find_num = int(input())
    for j in range (find_num) :
        u, v = map(int, input().split())
        if find(u) == find(v) :
            print(1)
        else :
            print(0)
    if i != testcase - 1 :
        print()

