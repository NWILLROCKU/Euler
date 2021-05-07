tri = 1
addMe = 2
numDiv = 1
#while numDiv <= 500:
for j in range(40):
    tri += addMe
    addMe += 1
    numDiv = 2 # 1 and tri
    fac = []
    for i in range(2, int(tri/2)+1):
        if tri % i==0:
            numDiv += 1
            fac.append(i)
    print(tri, numDiv, fac)
    
