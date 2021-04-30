# Read data from text file
a = []
with open('67_data.txt') as f:
    line = f.readline()
    n = len(line)
    while n > 0:
        a.append([])
        num = ''
        for i in range(n):
            if line[i] != ' ':
                num += line[i]
            if (i==n-1 or line[i]==' ') and len(num) > 0:
                a[-1].append(int(num))
                num = ''
        line = f.readline()
        n = len(line)

# Overwrite a with (maximum) cumulative sum
m = len(a)
for i in range(1,m):
    for j in range(i+1):
        if j==0:
            a[i][j] += a[i-1][j]
        elif j==i:
            a[i][j] += a[i-1][j-1]
        else:
            a[i][j] += max(a[i-1][j], a[i-1][j-1])
