
def fact(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n*fact(n-1)
        

def ssin(x):
    return (float(x) - float(x**3)/float(fact(3)) + float(x**5)/float(fact(5)))

def scos(x):
    return (float(1) - float(x**2)/float(fact(2))+ float(x**4)/float(fact(4)))
    
def stan(x):
    return ssin(x)/scos(x)

def ssec(x):
    return 1/scos(x)

def scsc(x):
    return 1/ssin(x)

def scot(x):
    return 1/stan(x)
    
