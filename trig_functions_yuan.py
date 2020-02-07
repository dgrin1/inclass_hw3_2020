import numpy as np
import math

def lsin(x):
#mod 2pi
	x = x % (2.e0*np.pi)
#initialize
	i = 0
	s,sold = 0.e0,0.e0
#keep at most 10000 terms in the Taylor series
	for i in range(1000):
		sold=s
		s+=float(((((-1)**i) * (x**((2*i)+1))))/float(math.factorial((2*i)+1)))
#if converged to machines precision then break out of loop
		if sold==s: break
	return s

def lcos(x):
#mod 2pi
        x = x % (2.e0*np.pi)
#initialize
        i = 0
        s,sold = 0.e0,0.e0
#keep at most 10000 terms in the Taylor series
        for i in range(1000):
                sold=s
                s+= float((((-1)**i) * (x**(2*i))))/float(math.factorial((2*i)))
#if converged to machines precision then break out of loop
                if sold==s: break
        return s

def ltan(x):
	return lsin(x)/lcos(x)

def lcot(x):
	return 1.e0/ltan(x)

def lsec(x):
	return 1.e0/lcos(x)

def lcsc(x):
	return 1.e0/lsin(x)

print(ltan(1))
print(np.tan(1))
print(lsec(1.570796326794896619))
print(lcsc(1.570))
