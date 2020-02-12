import numpy as np

#defining sine function

def f(x):
	val = np.sin(x)
	return val

#setting endpoints and number of values
N = 10
a = 0
b = 5

def riemann_linda(f,a,b,N):
	delta_x = (b-a)/N

#create empty list
	xvals = []
	yvals = []
	s = 0

#loop over all y vals
	for i in range (0,N+1,1):
		x = a+i*delta_x
		y = f(x)
		xvals.append(x)
		yvals.append(y)
		s+=y
	s+=delta_x
	return s
