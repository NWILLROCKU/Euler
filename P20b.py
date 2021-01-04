f = 36288
f_str = str(f)
i = 11
while i <= 100:
    f_str = str(f*i)
    f = int(f_str)
    i += 1

digit_sum = 0 
#f_str = str(f)
for i in range(len(f_str)):
    digit_sum += int(f_str[i])
