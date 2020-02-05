# Library with 6 trig functions: ssin, scos, stan, ssec, scsc, scot

#helper function factorial used in computing taylor approximations
def fact(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n*fact(n-1)
        
#three taylor terms
def ssin(x):
    return (float(x) - float(x**3)/float(fact(3)) + float(x**5)/float(fact(5)))

#three taylor terms
def scos(x):
    return (float(1) - float(x**2)/float(fact(2))+ float(x**4)/float(fact(4)))
    
# The next 4 functions are defined using scos and ssin
def stan(x):
    return ssin(x)/scos(x)

def ssec(x):
    return 1/scos(x)

def scsc(x):
    return 1/ssin(x)

def scot(x):
    return 1/stan(x)
    
