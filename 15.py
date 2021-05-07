a = [[1]*21]
for i in range(20):
    a.append([0]*21)
    a[-1][0] = 1
    for j in range(1, 21):
        a[-1][j] = a[-1][j-1] + a[-2][j]
