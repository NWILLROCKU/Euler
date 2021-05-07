year = 1900
month = 1
dayOfWeek = 2 # first of month

SunCnt = 0
while year < 2001:
    # Get month length
    if month==2:
        if year % 4==0:
            moLen = 29
        else:
            moLen = 28
    elif month==9 or month==4 or month==6 or month==11:
        moLen = 30
    else:
        moLen = 31

    dayOfWeek += (moLen % 7)
    if dayOfWeek > 7:
        dayOfWeek -= 7
    if dayOfWeek==1 and year > 1900:
        SunCnt += 1
        #print(year, month)

    month += 1
    if month > 12:
        month -= 12
        year += 1
