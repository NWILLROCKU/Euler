x = 1

def myfunc(a):
    global x
    x+=1
    print("Python is " + str(x))

myfunc(3)
