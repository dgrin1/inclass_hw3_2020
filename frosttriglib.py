#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np
import math

def fsin(x):
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
                if sold==s: break
        return s

def fcos(x):
    #initialize iterator and sum
        i = 0
        s,sold = 0.e0,0.e0

#Keep at most 10000 terms in the Taylor series
        for i in range(10000):
                sold=s
                s+= float((((-1)**i) * (x**((2*i) ))))/float(math.factorial(((2*i) )))
#If converged to machine precision then break out of loop
                if sold==s: break
        return s
    
def ftan(x):
    s = fsin(x)/fcos(x)
    return s

def fsec(x):
    s = 1/fcos(x)
    return s

def fcsc(x):
    s=1/fsin(x)
    return s

def fcot(x):
    s=fcos(x)/fsin(x)
    return s


# In[6]:


print(ftan(3))


# In[ ]:




