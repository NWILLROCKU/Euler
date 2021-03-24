diag_sum = 1
for i in range(3,1002,2):
    sideLength = i - 1
    diag_sum += 4*(i*i - 1.5*sideLength)
