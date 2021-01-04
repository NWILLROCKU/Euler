import math

plist = [2, 3, 5, 7, 11]
psum = 28
n = 13
while n < 2e6:
    root = math.sqrt(n)
    i = 1
    while plist[i] <= root:
        if n % plist[i] == 0:
            break
        i += 1

    if plist[i] > root:
        plist.append(n)
        psum += n
    n += 2
        
