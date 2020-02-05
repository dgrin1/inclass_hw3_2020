import numpy as np
import math

def gsin(x):
#take arg mod 2pi
    x=x%(2.e0*np.pi)
#initialize iterator and sum
    i = 0
    s,sold = 0.e0,0.e0

#Keep at most 10000 terms in the Taylor series
    for i in range(10000):
        sold=s
        s+= float((((-1)**i) * (x**((2*i) + 1))))/float(math.factorial(((2*i) + 1)))
#If converged to machine precision then break out of loop
        if sold==s: 
            break   
    return s


def gcos(x):
    
    # define iterator and sum
    i=0
    s,sold=0.,0.

    # set up taylor series with max. 10,000 terms
    for i in range(10000):
        sold=s
        s+=float( (-1)**i * ((x**(2*i))/float(math.factorial(2*i))  ))
        if sold==s: 
            break # quit loop if converged to machine precision
    return s


print(gcos(0))
print(gcos(np.pi))
