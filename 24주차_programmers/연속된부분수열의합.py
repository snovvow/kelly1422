import sys
input = sys.stdin.readline

def solution(sequence, k):
    start, end = 0, 0
    ans1, ans1, min_len = -1, -1, len(sequence)
    sum = sequence[0]
    while (start <= end) :
        if sum == k :
            if ans1 == -1 or min_len > end - start + 1 :
                ans1, ans2, min_len = start, end, end - start + 1
            end += 1
            if end >= len(sequence) :
                break
            sum += sequence[end]
            sum -= sequence[start]
            start += 1
        elif sum < k :
            end += 1
            if end >= len(sequence) :
                break
            sum += sequence[end]
        else :
            sum -= sequence[start]
            start += 1


    answer = [ans1, ans2]

    return answer

a = solution([2, 2, 2, 2, 2], 6)
print(a)