import time

def getDiv(n):
    # Gets all divisors of n, excluding n
    divList = [1]
    for i in range(2, int(n/2)+1):
        if n % i==0:
            divList.append(i)
    return divList

start_time = time.time()
maxab = 100#28200

# Get list of abundant nums
ab = []
for i in range(0, maxab + 1):
    if i%3000==0:
        print(i)
    
    if i % 2 > 0 and i % 5 > 0: # not divisible by 2 or 5
        continue
    if sum(getDiv(i)) > i:
        ab.append(i)
print('got list of ab in ' + str(time.time()-start_time) + ' seconds')

nonAb=[]
k= 0
for i in range(0, maxab + 1):
    if i%3000==0:
        print(i)
    while ab[k] < i:
        k += 1
    # Now ab[k] >= i
    k_orig = k
    j = 0
    while ab[j] <= i/2 and ab[k] >= i/2:
        if ab[j] + ab[k] > i:
            k -= 1
        elif ab[j] + ab[k] == i:
            break
        else:
            j += 1
    if ab[j] > i/2:
        nonAb.append(i)
    k = k_orig
print('got answer in ' + str(time.time()-start_time) + ' seconds')
#print(ab)
#print(nonAb)
