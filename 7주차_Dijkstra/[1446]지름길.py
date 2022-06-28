import sys
input = sys.stdin.readline

def sol() :
    n, d = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(n)] # [s, e, n] [1, 6, 4] [1, 7, 3]
    distance = [i for i in range(d + 1)]   # i번째 인덱스에는 ikm까지 가는 최단거리 저장
    # [0, 1, 2, 3, 4, 5, 3, 4, 8, 9, 10, ....., 150]

    for i in range(d + 1): # 지름길을 이용해 갈 수 있는 각 위치의 최단거리 업데이트 0 ~ d
        distance[i] = min(distance[i], distance[i - 1] + 1) # 직전 위치까지의 최단경로가 업데이트 되었다면, 그 길이 + 1로 업데이트
 
        for start, end, short in graph:
            if i == start and end <= d and distance[i] + short < distance[end]: # 지름길 경로중 현위치가 시작위치, 끝이 목표지점 넘지 않고, 경로 길이가 더 짧으면
                distance[end] = distance[i] + short

    print(distance[d])
    
sol()