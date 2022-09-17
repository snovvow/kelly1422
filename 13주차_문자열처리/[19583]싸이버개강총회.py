# import sys
# input = sys.stdin.readline

# time_str = input()
# time = time_str.replace(':', ' ')

# ahour, amin, bhour, bmin, chour, cmin = map(int, time.split())
# start = []
# end = []

# while True:
#     try:
#         chat_time, name = input().split()
#         h, m = map(int, chat_time.split(':'))
#         if h < ahour or (h == ahour and m <= amin) :
#             if name not in start :
#                 start.append(name)
#         elif (bhour < h < chour) or (h == bhour and m >= bmin) or (h == chour and m <= cmin) :
#             if (name in start) and (name not in end) :
#                 end.append(name)
#     except:
#         break

# print(len(end))

import sys
input = sys.stdin.readline

start, end, stream = input().split()
start = int(start[:2] + start[3:])
end = int(end[:2] + end[3:])
stream = int(stream[:2] + stream[3:])

before = set()
after = set()

while True:
    try:
        time, name = input().split()
        time = int(time[:2] + time[3:])
        if time <= start:
            before.add(name)
        elif end <= time <= stream and name in before:
            after.add(name)
    except:
        break

print(len(after))