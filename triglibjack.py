#importing math and numpy
import matplotlib.pyplot as plt
import numpy as np
import math
#defining the first trig equation of sine
x = float(input("give a number"))
def msin(x):
	x = x%(2.e0*np.pi)
	i = 0
	h,hold = 0.e0,0.e0
	
	for i in range (300):
		hold=h
		h+=float((((-1)**i)*(x**((2*i)+1))))/float(math.factorial(((2*i)+1)))
		if hold == h: break
	return h
#defining cos using the other series
def mcos(x):
	x = x%(2.e0*np.pi)
	i = 0
	h,hold = 0.e0,0.e0
	
	for i in range (300):
		hold=h
		h+=float((((-1)**i) * (x**(2*i))))/float(math.factorial(2*i))
		if hold == h: break
	return h
#defining tangent
def mtan(x):
	return msin(x)/mcos(x)

def msec(x):
	return  1/(mcos(x))
	
def mcot(x):
	return mcos(x)/msin(x)

def mcsc(x):
	return 1/(msin(x))

print(msin(x),mcos(x),mtan(x),msec(x),mcot(x),mcsc(x))
print(np.sin(x),np.cos(x),np.tan(x),1/(np.cos(x)),1/np.tan(x),1/np.sin(x))
print(np.sin(x)-msin(x),np.cos(x)-mcos(x))