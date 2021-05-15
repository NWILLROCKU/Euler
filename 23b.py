import time

def getDiv(n):
    # Gets all divisors of n, excluding n
    divList = [1]
    for i in range(2, int(n/2)+1):
        if n % i==0:
            divList.append(i)
    return divList

start_time = time.time()

# Get list of abundant nums
ab = [12]
maxab = 28121
for i in range(14, maxab):
    if i % 2 > 0 and i % 5 > 0: # not divisible by 2 or 5
        continue
    if sum(getDiv(i)) > i:
        ab.append(i)
print('got list of ab in ' + str(time.time()-start_time) + ' seconds')

nonAb=[24]
for i in range(25, 28124):
    j = 0
    while ab[j] < i:
        k = 0
        while ab[k] < i:
            if ab[j] + ab[k] == i:
                break
            k += 1
        if ab[k] < i:
            nonAb.append(i)
            break
        j += 1
print('got answer in ' + str(time.time()-start_time) + ' seconds')

