import numpy as np
import math

def taylorcos(x):
    x=x%(2.e0*np.pi)
    i=0
    S,oldS= 0.e0,0.e0


    for i in range(1000):
        oldS=S
        S+=float((((-1)**i) * (x**((2*i))))/float(math.factorial(((2*i)))))

        if oldS==S:
            break
    return S

x = int(input("Please enter your angle"))

print(taylorcos(x))
