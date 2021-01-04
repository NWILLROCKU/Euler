import math

nList = []
n = 0
while n < 399999:
    nstr = str(n)
    powsum = 0
    for i in nstr:
        powsum += int(i)**5
    if powsum==n:
        nList.append(n)
    if n % 10000==0:
        print(n)
    n += 1
