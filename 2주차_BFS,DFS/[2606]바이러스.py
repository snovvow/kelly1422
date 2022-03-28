computer = int(input())
network = int(input())

connect = [[0 for i in range (computer)] for j in range (computer)]
virus = [0 for i in range (computer)]

for i in range (network) :
    a, b = map(int, input().split())
    connect[a-1][b-1] = 1

def rec(n) :
    for i in range (computer) :
        if connect[n][i] == 1 or connect[i][n]:
            if virus[i] == 0 :
                virus[i] = 1
                rec(i)

rec(0)
virus[0] = 1
count = 0
for i in range (computer) :
    if virus[i] == 1 :
        count += 1
print(count - 1)
