def getCollatzLength(n):
    Clen = 1 # length of Collatz sequence
    while n > 1:
        if n % 2 == 0:
            n = n/2
        else:
            n = 3*n + 1
        Clen += 1
    return Clen

Clen_max = 1
n = 500e3
n_max = n
while n < 750002:
    Clen = getCollatzLength(n)
    if Clen > Clen_max:
        Clen_max = Clen
        n_max = n
    n += 1
    if n % 100e3==0:
        print(n)

numsinceskip = 1
n = 750003
while n < 1e6:
    Clen = getCollatzLength(n)
    if Clen > Clen_max:
        Clen_max = Clen
        n_max = n
    if numsinceskip==2:
        n += 2
        numsinceskip = 1
    else:
        n += 1
        numsinceskip += 1
    if n % 100e3==0:
        print(n)
