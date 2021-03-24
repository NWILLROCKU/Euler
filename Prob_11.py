file1 = open('Problem 11 data.txt', 'r')
Lines = file1.readlines()

data = []
for i in range(len(Lines)):
    line = []
    for j in range(20):
        line.append(int( Lines[i][3*j : 3*j+2] ))
    data.append(line)

##index = []
##for i in range(20):
##    try:
##        index.append(data[i].index(99))
##    except ValueError:
##        index.append(-1)
##    
