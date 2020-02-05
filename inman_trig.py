import numpy as np
import math

#SINE:
def ni_sin(x):
#converts x to radians?
	x=x%(2.e0*np.pi)
#initialize iterator and sum
	i = 0
	s,sold = 0.e0,1.e0
#Keep at most 1000 terms in the Taylor series
	while sold!=s:
		sold=s
		s+= float(((-1)**i) * (x**((2*i) + 1))/math.factorial((2*i) + 1))
		if sold == s: break
		if i > 1000: break
		i += 1
	return s

#COSINE:
def ni_cos(x):
#take arg mod 2pi
	x=x%(2.e0*np.pi)
#initialize iterator and sum
	i = 0
	q,qold = 0.e0,0.e0
#Calculate the result using a Taylor Series:
	for i in range(1000):
		qold=q
		q+= float(((-1)**i) * (x**((2*i)))/math.factorial(((2*i))))
#If converged to machine precision then break out of loop
		if qold==q: break
	return q

#TANGENT:
def ni_tan(x):
#take arg mod 2pi
	x=x%(2.e0*np.pi)
#initialize iterator and sum
	i = 0
	r,rold = 0.e0,0.e0
#Calculate the result using a Taylor Series:
	for i in range(1000):
		rold=r
		r+= ni_sin(x)/ni_cos(x)
#If converged to machine precision then break out of loop
		if rold==r: break
	return r
