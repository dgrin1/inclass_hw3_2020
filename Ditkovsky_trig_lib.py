import numpy as np
import math


def my_sin():
	x = float(input('in radians, x =  '))
	
	i = 0
	s, s_old = 0., 0.
	
	while i < 1000:
		s_old = s
		s += float((((-1)**i) * (x**((2*i) + 1))))/float(math.factorial(((2*i) + 1)))
		i += 1
		if s == s_old: break
		
	return(s)
	
def my_cos():

	x = float(input('in radians, x =  '))
	
	i = 0
	s, s_old = 0., 0.
	
	while i < 1000:
		s_old = s
		s += float((((-1)**i) * (x**((2*i)))))/float(math.factorial(((2*i))))
		i += 1
		if s == s_old: break
		
	return(s)
	
def my_tan():
	
	x = float(input('in radians, x =  '))
	
	sin = my_sin(x)
	cos = my_cos(x)
	
	tan = sin/cos
	
	return(tan)
	
	
def my_cot():
	
	x = float(input('in radians, x =  '))
	
	sin = my_sin(x)
	cos = my_cos(x)
	
	cot = cos/sin
	
	return(cot)
	
def my_sec():
	
	x = float(input('in radians, x =  '))
	
	cos = my_cos(x)
	
	sec = 1./cos
	
	return(sec)
	
def my_csc():

	x = float(input('in radians, x =  '))
	
	sin = my_sin(x)
	
	csc = 1./sin
	
	return(csc)