import numpy as np

def f(x):
	val=x**(4) -2*x +1

N=100000
a=0
b=2


def riemann_hartman(f,a,b,N):
	delta_x = (b-a)/N
	
	xvals=[]
	yvals=[]
	s=0
	
	for i in range(0,N,1):
		x=a+i*delta_x
		
		y=f(x)
		
		xvals.append(x)
		yvals.append(y)
		
		s+=y
		
	s*=delta_x
	return s
	
	
	
#def simpson_hartman(f,a,b,N):



#def trapazoid_hartman(f,a,b,N):
	delta_x2 = (b-a)/N
	
	xvals2=[]
	yvals2=[]
	
	for i in range(0,N,1):
		x=