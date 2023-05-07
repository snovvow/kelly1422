import sys
input = sys.stdin.readline

money = int(input())

price = list(map(int, input().split()))

def bnp(money, price) :
    sum = 0
    for i in range(14) :
        if money // price[i] > 0 :
            sum += money // price[i]
            money = money % price[i]
    return money + (price[-1] * sum)

def timing(money, price) :
    increase, decrease, sum = 0, 0, 0
    for i in range(1, 14) :
        if price[i - 1] < price[i] :
            decrease = 0
            increase += 1
        elif price[i - 1] > price[i] :
            decrease += 1
            increase = 0
        else :
            decrease = 0
            increase = 0
        
        if increase >= 3 :
            money += sum * price[i]
            sum = 0
        if decrease >= 3 :
            sum += money // price[i]
            money = money % price[i]
    return money + (price[-1] * sum)

re_bnp = bnp(money, price)
re_timing = timing(money, price)

if re_bnp > re_timing :
    print("BNP")
elif re_bnp < re_timing :
    print("TIMING")
else :
    print("SAMESAME")