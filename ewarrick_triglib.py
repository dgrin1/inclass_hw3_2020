#make a sin, cos, tan library of trig functions
#using code from dgrin/inclass_hw3_2020/sinx_best_for_func.py
#collab: Nina Inman

import numpy as np
import math

#sine
def ewar_sin(x):
#take arg mod 2pi
	x=x%(2.e0*np.pi)
#initialize iterator and sum
	i = 0
	s,sold = 0.e0,0.e0

#Keep at most 10000 terms in the Taylor series
	for i in range(1000):
		sold=s
		s+= float((((-1)**i) * (x**((2*i) + 1))))/float(math.factorial(((2*i) + 1)))
#If converged to machine precision then break out of loop
		if sold==s: break
	return s
	
#cosine
def ewar_cos(x):
#take arg mod 2pi
	x=x%(2.e0*np.pi)
#initialize iterator and sum
	i = 0
	c,cold = 0.e0,0.e0

#Keep at most 10000 terms in the Taylor series
	for i in range(1000):
		cold=c
		c+= float((((-1)**i) * (x**((2*i)))))/float(math.factorial(((2*i))))
#If converged to machine precision then break out of loop
		if cold==c: break
	return c
	
#tangent
def ewar_tan(x):
#take arg mod 2pi
	x=x%(2.e0*np.pi)
#initialize iterator and sum
	i = 0
	t,told = 0.e0,0.e0

#Keep at most 10000 terms in the Taylor series
	for i in range(1000):
		told=t
		t+= (ewar_sin(x))/(ewar_cos(x))
#If converged to machine precision then break out of loop
		if told==t: break
	return t