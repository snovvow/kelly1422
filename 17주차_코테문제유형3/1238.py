import sys
import heapq
input = sys.stdin.readline
INF = float('inf')

N, M, X = map(int, input().split())
dis = [[] for _ in range (N + 1)]

for i in range (M) :
    start, end, value = map(int, input().split())
    dis[start].append((value, end))

def dijkstra(start) :
    q = []
    heapq.heappush(q, (0, start))
    distance = [INF] * (N + 1)
    distance[start] = 0

    while q :
        value, dest = heapq.heappop(q)

        if value > distance[dest] :
            continue
        
        for diff, node in dis[dest] :
            new_value = distance[dest] + diff
            if distance[node] > new_value :
                distance[node] = new_value
                heapq.heappush(q, (new_value, node))
    return distance

back = dijkstra(X)
longest = 0
for i in range (1, N + 1) :
    if i != X :
        go = dijkstra(i)
        longest = max(longest, go[X] + back[i])

print(longest)

# import sys
# input = sys.stdin.readline
# INF = float('inf')

# N, M, X = map(int, input().split())
# dis = [[INF for _ in range (N)] for _ in range (N)]

# for i in range (M) :
#     start, end, value = map(int, input().split())
#     dis[start-1][end-1] = value

# def dijkstra(node, dest) :
#     visited = [False] * N
#     visited[node] = True
#     for i in range (N - 2) :
#         mini = INF
#         mid = 0
#         for j in range (N) :
#             if j != dest and not visited[j] and mini > dis[node][j] :
#                 mid = j
#                 mini = dis[node][j]
#         visited[mid] = True
#         for r in range (N) :
#             if not visited[r] :
#                 if dis[node][r] > dis[node][mid] + dis[mid][r]:
#                     dis[node][r] = dis[node][mid] + dis[mid][r]

# longest = 0
# X = X - 1

# for i in range (N) :
#     if i != X :
#         dijkstra(X, i)
        
# for i in range (N) :
#     if i != X :
#         dijkstra(i, X)
#         if dis[i][X] != INF and dis[i][X] > longest :
#             longest = dis[i][X]

# for i in range (N) :
#     if i != X :
#         if dis[i][X] != INF and dis[X][i] != INF :
#             if dis[i][X] + dis[X][i] > longest :
#                 longest = dis[i][X] + dis[X][i]

# print(longest)

# 4 8 2
# 1 2 4
# 1 3 2
# 1 4 7
# 2 1 1
# 2 3 5
# 3 1 2
# 3 4 4
# 4 2 3