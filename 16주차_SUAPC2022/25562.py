import sys
input = sys.stdin.readline

N = int(input())
print((N * (N - 1)) // 2)
x = 1
for i in range(N - 1) :
    print(x, end=' ')
    x *= 2
print(x)

print(N - 1)
for i in range (1, N) :
    print(i, end=" ")
print(N) 
