def factorial(num):
    if num==0:
        return 1
    else:
        return num*factorial(num-1)

fac = 9
diff = 1e6-1#1e6
digits_used = []
digits_avail = [0,1,2,3,4,5,6,7,8,9]
while len(digits_avail) > 0:
    nextDig = int(diff / factorial(fac))
    diff -= factorial(fac) * nextDig
    digits_used.append(digits_avail[nextDig])
    digits_avail.pop(nextDig)
    fac -= 1

print(digits_used)
