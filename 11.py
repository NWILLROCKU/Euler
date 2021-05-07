# Read data from text file
a = []
with open('11_data.txt') as f:
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

max_prod = 1

# left right
for i in range(len(a)):
    for last_j in range(3, len(a[0])):
        prod = 1
        for j in range(last_j-3, last_j+1):
            prod *= a[i][j]
        max_prod = max(max_prod, prod)

# up down
for last_i in range(3, len(a)):
    for j in range(len( a[0] )):
        prod = 1
        for i in range(last_i-3, last_i+1):
            prod *= a[i][j]
        max_prod = max(max_prod, prod)

# upper left - bottom right
for last_i in range(3, len(a)):
    for last_j in range(3, len(a[0])):
        prod = 1
        i = last_i
        j = last_j
        for k in range(4):
            prod *= a[i][j]
            i -= 1
            j -= 1
        max_prod = max(max_prod, prod)

# bottom left - upper right
for last_i in range(3, len(a)):
    for last_j in range(3, len(a[0])):
        prod = 1
        i = last_i
        j = last_j-3
        for k in range(4):
            prod *= a[i][j]
            i -= 1
            j += 1
        max_prod = max(max_prod, prod)

print(max_prod)
