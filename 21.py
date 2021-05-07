def getDiv(n):
    # Gets all divisors of n, excluding n
    divList = [1]
    for i in range(2, int(n/2)+1):
        if n % i==0:
            divList.append(i)
    return divList

Am = []
notAm = []
maxAm = 9999
for i in range(1, maxAm+1):
    if i in Am or i in notAm:
        continue
    mysum = sum(getDiv(i))
    if sum(getDiv(mysum))==i and i != mysum:
        Am.append(i)
        if mysum <= maxAm:
            Am.append(mysum)
    else:
        notAm.append(i)
