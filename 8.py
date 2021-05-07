# Read data from text file
a = []
with open('8_data.txt') as f:
    line = f.readline()
    while len(line) > 0:
        a.append([])
        for char in line:
            try:
                a[-1].append(int(char))
            except:
                break
        line = f.readline()

# Overwrite a with (maximum) cumulative sum
max_prod = 0
for row in a:
    for last_i in range(12, len(row)):
        first_i = last_i - 12
        prod = 1
        for i in range(first_i, last_i + 1):
            prod *= i
        max_prod = max(prod, max_prod)
        


