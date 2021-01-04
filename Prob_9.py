import math

##i = 333
##a = math.sqrt(2*i+1)
##
##def dome(i):
##    a = math.sqrt(2*i+1)
##    while (a != round(a)):
##        i += 1
##        a = math.sqrt(2*i+1)
##    return [i, a + a*a]
##
##dome(i)

c=499
i = 500-c
a_start = 250
b_start = 251
a = a_start
b = b_start
while (a*a + b*b != c*c):
    if a==2*i+1:
        c-=1
        i = 500-c
        if c % 2==0:
            b_start += 1
        else:
            a_start += 1
        a = a_start
        b = b_start
    else:
        a -= 1
        b += 1
        
