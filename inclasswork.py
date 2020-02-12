import numpy and np
import math

def msin(x):
	x = x%(2.e0*np.pi)
	i = 0
	h,hold = 0.e0,0.e0
	
	for i in range (100):
		hold=h
		h+=float((((-1)**i)*(x**((2*i)+1))))/float(math.factorial(((2*i)+1)))
		if hold == h: break
	return h
	
def mcos(x):
	x = x%(2.e0*np.pi)
	i = 0
	h,hold = 0.e0,0.e0
	
	for i in range (100):
		hold=h
		h+=float((((-1)**i) * (x**(2*i))))/float(math.factorial(2*i))
		if hold == h: break
	return h
	
def mtan(x):
	