import sys
input = sys.stdin.readline

def solution(targets):
    answer = 0
    sort_t = sorted(targets, key= lambda x:x[1])

    i = 0
    while (i < len(sort_t)) :
        end = sort_t[i][1]
        answer += 1
        while (i < len(sort_t) - 1) :
            if end > sort_t[i+1][0] :
                i += 1
            else :
                break
        i += 1
    
    return answer

print(solution([[4,5],[4,8],[10,14],[11,13],[5,12],[3,7],[1,4]]))