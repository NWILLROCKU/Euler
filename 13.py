mynum = 0
with open('13_data.txt') as file:
    a=file.readline()
    while len(a) > 0:
        mynum += int(a[:-1])
        print(a)
        print(mynum)
        b=a
        a=file.readline()
