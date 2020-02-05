import math
import numpy as np

def mysin(x):
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


def mycos(x):
	x = x%(2.0*np.pi)
	s, s_old = 0.e0, 0.e0

	for n in range (10000):
		s_old = s
		s += float((-1)**(n)*(x**(2*n)))/float(math.factorial(2*n))

		if s_old==s: 
			break
	return s

def mytan(x):
	return float(mysin(x)/mycos(x))

def mycot(x):
	return float(mycos(x)/mysin(x))

def sec(x):
	return float(1/mycos(x))

def csc(x):
	return float(1/mysin(x))