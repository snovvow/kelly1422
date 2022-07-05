import sys
input = sys.stdin.readline

str = input().strip()
stack = []
ppap = ["P", "P", "A", "P"]
for i in range(len(str)):
    stack.append(str[i])
    if stack[-4:] == ppap:
        for _ in range(3):
            stack.pop()
if stack == ppap or stack == ["P"]:
    print("PPAP")
else:
    print("NP")

# while True :
#     before_len = len(ppap)
#     ppap = ppap.replace("PPAP", 'P')
#     after_len = len(ppap)
#     if before_len == after_len :
#         break

# if ppap == "P" :
#     print("PPAP")
# else :
#     print("NP")