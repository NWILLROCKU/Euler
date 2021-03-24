import time

t1 = time.time()
powerFamilies = [[2,4,8,16,32,64],
                 [3,9,27,81],
                 [5,25],
                 [6,36],
                 [7,49],
                 [10,100]]

powersOfTwo = []
for exp in range(2,101):
    powersOfTwo.append(pow(2, exp))
    
powersOfFour = []
base = powerFamilies[0][1]
for exp in range(2,101):
    if pow(base, exp) not in powersOfTwo:
        powersOfFour.append(pow(base, exp))

powersOfTwoFamily = [powersOfTwo, powersOfFour]
for base in powerFamilies[0][2:]:
    nextPowersOf = []
    for exp in range(2,101):
        myPow = pow(base, exp)
        for powersOf in powersOfTwoFamily:
            if myPow > powersOf[-1]:
                continue
            if myPow in powersOf:
                skipFlag = 1
                break
        if skipFlag==1:
            skipFlag = 0
            continue
        else:
            nextPowersOf.append(myPow)
    powersOfTwoFamily.append(nextPowersOf)


##powers = []
##for base in range(2,101):
##    for exp in range(2,101):
##        myPow = pow(base, exp)
##        if myPow not in powers:
##            powers.append(myPow)
print(time.time() - t1)
