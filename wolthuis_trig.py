
# coding: utf-8

# In[21]:


import numpy as np
import math

def wsin(x):
#take arg mod 2pi
    x= x%(2.e0*np.pi)
#initialize iterator and sum
    i = 0
    s, sOLD = 0.e0, 0.e0

#Keep at most 10000 terms in Taylor Series
    for i in range(100):
        sOLD = s
        s += float(((((-1) ** i) * (x ** ((2*i) + 1 )))) / float(math.factorial(((2*i) + 1))))
    #if converged to machine precision then break out
        if sOLD == s: 
            break
    return s


# In[19]:


def wcos(x):
#take arg mod 2pi
    x = get_ipython().run_line_magic('(2.e0*mp.pi)', '')
#initialize iterator and sum
    i = 0
    s, s0 = 0.e0, 0.e0
    
#Keep at most 10000 terms in Taylor Series
    for i in range(100):
        s0 = s
        s += float((((-1) ** i) * (x ** (2*i)))) / float(math.factorial(2*i))
    #if converged to machine precision then break out
        if s0 == s: 
            break
    return s


# In[9]:


def wtan(x):
    #using the previously defined functions
    return((wsin(x))/(wcos(x)))


# In[15]:


def wcot(x):
    #using the tan function
    return(1/ wtan(x))


# In[17]:


def wsec(x):
    #using the cos command
    return(1/(wcos(x)))


# In[18]:


def wcsc(x):
    #using the sin command
    return (1/wsin(x))

