import sys
input = sys.stdin.readline

def differ(team_list) :
    another_list = list(set(range(N)) - set(team_list)) #set 자료구조를 통해 입력된 팀 선수들의 인덱스로 부터 상대팀의 선수들의 인덱스를 구한다
    team = 0
    for i, v in enumerate(team_list[:-1]):
        for v2 in team_list[i+1:]:
            team += ability[v][v2] + ability[v2][v]
    
    another = 0
    for i, v in enumerate(another_list[:-1]): #인덱스와 원소로 이루어진 튜플(tuple)을 만들어줌
        for v2 in another_list[i+1:]:
            another += ability[v][v2] + ability[v2][v]
    
    ans.append(abs(team - another)) # 차이니까 절대값

def dfs(team_list) :
    if len(team_list) == N/2:
        differ(team_list)
        return None
    
    for i in range(team_list[-1] if team_list else 0, N):
        if team_list and team_list[0] != 0:
          return None
        if i not in team_list:
            team_list.append(i)
            dfs(team_list)
            team_list.pop()

N = int(input())
ability = [list(map(int, input().split())) for _ in range(N)]
ans = []
dfs([])
print(min(ans)) # 가능한 모든 차이중 최소