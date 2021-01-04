import math

nList = []
n = 0
while n < 29999:
    nstr = str(n)
    powsum = 0
    for i in nstr:
        powsum += int(i)**4
    if powsum==n:
        nList.append(n)
    if n % 1000==0:
        print(n)
    n += 1
