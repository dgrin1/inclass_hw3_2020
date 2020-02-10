#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[22]:


def f(x):
	val=x**4-2*x+1
	return val

#setting endpoints and number of values
N=1000000
a=0.
b=5.

def riemann_dan(f,a,b,N):
#setting bin width
	delta_x=(b-a)/N

#Create empty list
	xvals=[]
	yvals=[]
	s=0

#Loop over all y values
	for i in range(0,N,1):
#set x value at left edge of bin
		x=a+i*delta_x
#set function value of bin
		y=f(x)
#append x and y to list
		xvals.append(x)
		yvals.append(y)
#increment sum	
		s+=y
	s*=delta_x
	return s


def trapezoid(f,a,b,N):
    h = (b-a)/N
    fa = f(a)
    fb = f(b)
    y = 0
    for i in range(1,N,2):
        y += (f(a+i*h)+f(a+(i+1)*h))
    s = h*(.5*fa + .5*fb + y)
    return s
        
    
        
def simpson(f,a,b,N):
    h = (b-a)/N
    fa = f(a)
    fb = f(b)
    y1 = 0
    y2 = 0
    for i in range(1,N,2):
        y1+= f(a+i*h)
    for i in range(2,N-1,2):
        y2 += f(a+i*h)
    s = 1/3*h*(fa + fb + 4*y1 + 2*y2)
    return s
        
    
    


# In[23]:


print(simpson(f,0,2,1000))


# In[ ]:




