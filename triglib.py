import numpy as np
import math
from triglib import *

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
		if sold==s: break
	return s

def gcos(x):
#take arg mod 2pi
	x=x%(2.e0*np.pi)
#initialize iterator and sum
	i = 0
	s,sold = 0.e0,0.e0

#Keep at most 10000 terms in the Taylor series
	for i in range(10000):
		sold=s
		s+= float(((-1)**i) * (x**(2*i)))/float(math.factorial(2*i))
#If converged to machine precision then break out of loop
		if sold==s: break
	return s
	
def gtan(x): return gsin(x)/gcos(x)
	
def gsec(x): return 1./gcos(x)
def gcsc(x): return 1./gsin(x)
def gcot(x): return gcos(x)/gsin(x)
