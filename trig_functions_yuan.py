import numpy as np
import math

def lsin(x):
#mod 2pi
	x = x % (2.*np.pi)
#initialize
	i = 0
	s, sold = 0.,0.
#keep at most 10000 terms in the Taylor series
	for i in range(2):
		sold=s
		s+=float((((-1)**i) * (x**((2*i)+1)))/float(math.factorial((2*1)+1)))
#if converged to machines precision then break out of loop
		if sold==s: break
		return s
print(lsin(0.5))
print(np.sin(0.5))
