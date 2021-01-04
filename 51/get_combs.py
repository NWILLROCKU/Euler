opComplete = 0 # flag for whether all combinations have been produced
nList = ['0000']
while 1:
    n = nList[-1]
    index = len(n) - 1
    while n[index] != '0':
        index -= 1
        if index < 0:
            opComplete = 1
            break
    if opComplete==1:
        break
    else:
        orig_length = len(n)
        n = n[0:index] + '*'
        for i in range(orig_length - 1 - index):
            n += '0'
        nList.append(n)

nrows = len(nList) / 4
for i in range(int(nrows)):
    print(nList[4*i] + '\t' + nList[4*i+1] + '\t' + nList[4*i+2] + '\t' + nList[4*i+3] + '\n')
