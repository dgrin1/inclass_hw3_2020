import numpy as np
import math

#defines sine
def jsin(x):

	x=x%(2.e0*np.pi)
	i=0
	s,sold=0.e0,0.e0
	
	for i in range(1000):
		sold=s
		s+=float((((-1)**i)*(x**((2*i)+1))))/float(math.factorial(((2*i)+1)))
		
		if sold==s: 
				break
	return s

#defines cosine	
def jcos(x):
	x=x%(2.e0*np.pi)
	i=0
	c,cold=0.e0,0.e0
	
	for i in range(1000):
		cold=c
		c+=float(1 + (((-1)**i)*(x**((2*i)))))/float(math.factorial(((2*i))))
		
		if cold==c:
				break
	return c

#defines tangent
def jtan(x):
	t = jsin(x)/jcos(x)
	return t

#defines sinh
def jsinh(x):

	x=x%(2.e0*np.pi)
	i=0
	s,sold=0.e0,0.e0
	
	for i in range(1000):
		sold=s
		s+=float((((1)**i)*(x**((2*i)+1))))/float(math.factorial(((2*i)+1)))
		
		if sold==s: 
				break
	return s
	
#defines cosh
def jcosh(x):
	x=x%(2.e0*np.pi)
	i=0
	c,cold=0.e0,0.e0
	
	for i in range(1000):
		cold=c
		c+=float(1 + (((1)**i)*(x**((2*i)))))/float(math.factorial(((2*i))))
		
		if cold==c:
				break
	return c
	
#defines tanh
def jtanh(x):
	t = jsinh(x)/jcosh(x)
	return t