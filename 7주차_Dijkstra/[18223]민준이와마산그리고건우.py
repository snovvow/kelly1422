import heapq # 이진 트리(binary tree) 기반의 최소 힙(min heap) 자료구조
import sys
input = sys.stdin.readline


V, E, P = map(int, input().split()) 
node = [[] for _ in range(V + 1)] # 노드(정점)의 수만큼 배열, 배열의 각 요소는 [갈수 있는 노드 번호, 길이]의 배열로 이루어짐 node[1] -> [[2, 3], [5, 1]]
for _ in range(E):
    a, b, c = map(int, input().split())
    node[a].append([b, c]) # "a번째 노드에서 b로 c길이를 거쳐 갈 수 있음" , a랑 연결된게 있으면 또 append
    node[b].append([a, c]) # 양방향 그래프이므로, 두 정점 모두 출발지로 추가

inf = float('inf') 
distance = [inf] * (V + 1) # 각 노드로 가는 최단 경로 저장

visit = [False] * (V + 1) # 최단 경로를 탐색할때 이미 방문한 노드를 bool 값으로 표시
queue = [] 
heapq.heappush(queue, [0, 1, 1]) # 가장 먼저 시작점인, 1번 노드를 큐에 추가 (항상 정렬된 상태로 추가되고 삭제)
# [현재까지 지나온 경로 길이, 노드 번호, 건우를 지났는지]

while queue: # 깊이 우선도 아니고, 그냥 경로가 추가될떄마다 제일 짧은 길부터 탐색
    long, node_num, gunwoo = heapq.heappop(queue) # 가장 작은, 현재까지 최단경로인것을 pop
    if node_num == V : # 도착 노드면 break (long 값이, 지금 갈수 있는 노드중 가장 최단 경로 and 도착 노드 -> 최단 경로다)
        break

    print(visit)
    if visit[node_num] == False: # 아직 방문하지 않은 노드라면 (이미 방문했다는 말은 그 노드를 도착하는 더 짧은 경로가 있었다는 말, 더 긴 경로 체크할 필요없음)
        visit[node_num] = True # 근데 바꾼 다음 다시 False를 안해줘도 되는가? -> 어차피 이 노드를 지나는 최단경로는 현재 경로 이기 때문 그럴 필요없음
        distance[node_num] = long
        if node_num == P: # 건우가 있는 노드를 지나면 
            gunwoo = 0
        for nxt, d in node[node_num]: # 현재 노드에서 갈 수 있는 다음 노드 다 체크
            if visit[nxt] == False:
                heapq.heappush(queue, [long + d, nxt, gunwoo])
        print(queue)

    print("----------------------")

if gunwoo == 0:
    print('SAVE HIM')
else:
    print('GOOD BYE')
    