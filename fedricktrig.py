# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 12:54:30 2020

@author: shaun
"""
import numpy as np
import math
def ssin(x):
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
#just modifies the taylor series dan found for sin(x)
def scos(x):
#take arg mod 2pi
	x=x%(2.e0*np.pi)
#initialize iterator and sum
	i = 0
	s,sold = 0.e0,0.e0

#Keep at most 10000 terms in the Taylor series
	for i in range(10000):
		sold=s
		s+= float((((-1)**i) * (x**((2*i)))))/float(math.factorial(((2*i))))
#If converged to machine precision then break out of loop
		if sold==s: break
	return s
#divide sin(x) by cos(x) to get tan
def stan(x):
    result=sin(x)/cos(x)
    return result
#reciprocal of cos
def ssec(x):
    result=1/cos(x)
    return result
#reciprocal of sine
def scosec(x):
    result=1/sin(x)
    return result
#reciprocal of tan
def scotan(x):
    result=1/tan(x)
    return result