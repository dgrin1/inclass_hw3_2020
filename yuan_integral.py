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
	delta_x = float((b-a)/N)

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

#trapezoidal
def trap_linda(f,a,b,N):
	delta_x = float((b-a)/N)
	s = 0.0
	for i in range(1,N):
		s+=f(a+delta_x*i)
	s+=(1/2)*(f(a)+f(b))
	s*=delta_x
	return s

#simpsons
def linda_simpson(f,a,b,N):
	delta_x = float((b-a)/N)
	odds = 0.0
	evens = 0.0
	s = 0.0
	for i in range(1,N,2):
		odds+=f(a+delta_x*i)
	for j in range(2,N,2):
		evens+=f(a+delta_*j)
	s = (1/3)*delta_x*(f(a)+f(b)+4*odds+2*evens)
