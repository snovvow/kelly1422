import sys
input = sys.stdin.readline

N = int(input())
cards = list(map(int, input().split()))

f_cards = [0] * N
f_cards[0] = cards[0]
f_cards[1] = cards[1]
for i in range (N // 2) :
    f_cards[i * 2] = cards[i * 2] + f_cards[i * 2 - 2]
    f_cards[i * 2 + 1] = cards[i * 2 + 1] + f_cards[i * 2 - 1]

b_cards = [0] * N
b_cards[N - 1] = cards[N - 1]
b_cards[N - 2] = cards[N - 2]
for i in range (N // 2 - 2, -1, -1) :
    b_cards[i * 2] = cards[i * 2] + b_cards[i * 2 + 2]
    b_cards[i * 2 + 1] = cards[i * 2 + 1] + b_cards[i * 2 + 3]

max_sum = b_cards[0]

for i in range (N - 1) :
    if i == 0 :
        max_sum = max(max_sum, b_cards[1])
    elif i % 2 == 0 : # 내 차례
        max_sum = max(max_sum, f_cards[i - 2] + b_cards[i + 1])
    else :
        max_sum = max(max_sum, f_cards[i - 1] + b_cards[i] - b_cards[-1])

print(max_sum)

