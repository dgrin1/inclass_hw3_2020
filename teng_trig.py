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

def gtan(x):
    return float(gsin(x)/gcos(x))

def gsec(x):
    return float(1/gcos(x))

def gcsc(x):
    return float(1/gsin(x))

def gcot(x):
    return float(1/gtan(x))

import matplotlib.pyplot as plt

x=np.linspace(0.001,2*np.pi-0.001,1000)
functions=['sin','cos','tan','csc','sec','cot']
outputs=[[],[],[],[],[],[]]
colors=plt.cm.viridis(np.linspace(0,1,6))

for i in x:
    outputs[0].append(gsin(i))
    outputs[1].append(gcos(i))
    outputs[2].append(gtan(i))
    outputs[3].append(gcsc(i))
    outputs[4].append(gsec(i))
    outputs[5].append(gcot(i))

plt.figure()

for i in range(6):
    plt.scatter(x,outputs[i],c=colors[i],label=functions[i],marker=".")
plt.ylim(-2,2)
plt.legend()
plt.show()