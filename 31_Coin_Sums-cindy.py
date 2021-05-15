target = 200 # target sum
possCoins = [200, 100, 50, 20, 10, 5, 2, 1]

table = [200]
#combs = [[200]]
combCnt = 1
while table[0] != 1:
    lastCoin = table.pop()
    while lastCoin==min(possCoins):
        lastCoin = table.pop()
    while sum(table) < target:
        for i in range(possCoins.index(lastCoin) + 1, len(possCoins)):
            coin = possCoins[i]
            #
    combCnt += 1
