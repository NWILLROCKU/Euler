# Read data from text file
a = []
with open('8_data.txt') as f:
    line = f.readline()
    while len(line) > 0:
        for char in line:
            try:
                a.append(int(char))
            except:
                break
        line = f.readline()

# Overwrite a with (maximum) cumulative sum
max_prod = 0
for last_i in range(12, len(a)):
        first_i = last_i - 12
        prod = 1
        for i in range(first_i, last_i + 1):
            prod *= a[i]
#max_prod = max(prod, max_prod)
        if prod > max_prod:
            max_prod = prod
            digits = a[first_i : last_i+1]
        
        


