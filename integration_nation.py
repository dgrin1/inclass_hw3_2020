#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Riemann sum method
import numpy as np

def f(x):
	val=x**4-2*x+1
	return val	

#setting endpoints and number of values
N=1000000
a=0.
b=2.

def riemann_skd(f,a,b,N):
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

print("the Riemann approximation for this integral is:" ,riemann_skd(f,a,b,N))


# In[5]:


#Trapezoid method
import numpy as np

def f(x):
    return x**4-2*x+1

N=10
a=0.
b=2.
h=(b-a)/N

s=0.5*f(a)+0.5*f(b) #the two sides of the trapezoid

for i in range(1,N):
    s+=f(a+i*h)
    
print(h*s)


# In[16]:


#Simpsons method
import numpy as np

def f(x):
    return x**4-2*x+1

N=10

# Newman p146 method
def simp_skd(f,a,b,N):
    sum1=0.0
    sum2=0.0
    sum3=0.0
    delta_x=(b-a)/N
    # Odd terms 
    for k in range(1,N,2):
        sum1+=f(a+k*delta_x)
    # Even terms
    for k in range(2,N,2):
        sum2+=f(a+k*delta_x)
    # Finalize the sum
    sum3 = (1/3)*delta_x*(4*sum1+2*sum2+f(a)+f(b))
    return sum3

# error?
print(simp_skd(f,1,2,N))
print("Difference from the theoretical value is: ",abs(simp_skd(f,1,2,N)-4.4))
print("\n")


# In[ ]:




