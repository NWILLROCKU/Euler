import math

tri = 1
addMe = 2
numDiv = 1
#while numDiv <= 500:
for j in range(40):
    tri += addMe
    addMe += 1
    numDiv = 2 # 1 and tri
    for i in range( 2, int(math.sqrt(tri))+1 ):
        if tri % i==0:
            numDiv += 2
            #fac.append(i)
    if math.sqrt(tri)==int(math.sqrt(tri)):
        numDiv -= 1
    print(tri, numDiv)
    
