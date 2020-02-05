import numpy as np
import math

#define a function to compute sin using the taylor approximation
def my_sin(x): #takes x in radians)
	
	x=float(x%(2*np.pi))
	i = 0
	s, s_old = 0., 0.
	
	while i < 1000:
		s_old = s
		s += float((((-1)**i) * (x**((2*i) + 1))))/float(math.factorial(((2*i) + 1)))
#break when next term is negligible
		i += 1
		if s == s_old: break
		
	return(s)

#define a function to compute cis using the taylor approximation	
def my_cos(x):
	x=float(x%(2*np.pi))
	i = 0
	c, c_old = 0., 0.
	
	while i < 1000:
		c_old = c
		c += float((((-1)**i) * (x**((2*i)))))/float(math.factorial(((2*i))))
#break when next term is neglibible	
		i += 1
		if c == c_old: break
		
	return(c)
	
#define a function to compute tan using functions for sin and cos
def my_tan(x):
	x=float(x%(2*np.pi))
	sin = my_sin(x)
	cos = my_cos(x)
	
	tan = sin/cos
	
	return(tan)
	
#define a function to compute tan using functions for sin and cos	
def my_cot(x):
	x=float(x%(2*np.pi))
	sin = my_sin(x)
	cos = my_cos(x)
	
	cot = cos/sin
	
	return(cot)

#define a function to compute sec using function for cos
def my_sec(x):
	
	x=float(x%(2*np.pi))
	cos = my_cos(x)
	
	sec = 1./cos
	
	return(sec)
	
#define a function to compute csc using function for sin
def my_csc(x):

	x=float(x%(2*np.pi))
	sin = my_sin(x)
	
	csc = 1./sin
	
	return(csc)
