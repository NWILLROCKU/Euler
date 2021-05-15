def dec2bin(n):
    if n==0:
        return '0'
    x = 0
    while 2**x < n:
        x += 1
    # Now 2^x >= n
    diff = n # remaining 
    binStr = '' # binary string
    while x >= 0:
        if 2**x > diff:
            if len(binStr) > 0:
                binStr += '0'
        else:
            binStr += '1'
            diff -= 2**x
        x -= 1
    return binStr

doubleBasePalList = []
i = 1
while i < 1e6:
    decStr = str(i)
    if decStr==decStr[::-1]:
        binStr = dec2bin(i)
        if binStr==binStr[::-1]:
            doubleBasePalList.append(i)
    i += 2
        
