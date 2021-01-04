f = 36288
f_str = str(f)
i = 11
while i <= 100:
    i_str = str(i)
    if i_str[1]=='2':
        fac2 = i / 2;
    elif i_str[1]=='5':
        fac5 = i / 5;
        #f *= fac2 * fac5
        f_str = str(f * fac2 * fac5)
        f = int(f_str)
    elif i_str[1] != '0':
        #f *= i
        f_str = str(f * i)
        f = int(f_str)
    i += 1

digit_sum = 0 
#f_str = str(f)
for i in range(len(f_str)):
    digit_sum += int(f_str[i])
