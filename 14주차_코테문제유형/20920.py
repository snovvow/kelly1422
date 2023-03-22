import sys
input = sys.stdin. readline

N, M = map(int, input().split())
dictionary = {}
for i in range (N) :
    word = input().strip()
    if len(word) >= M :
        if word in dictionary :
            dictionary[word] += 1
        else :
            dictionary[word] = 1

dictionary = sorted(dictionary, key= lambda x : (-dictionary[x], -len(x), x))
print(*dictionary, sep="\n")
