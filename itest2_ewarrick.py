#elizabeth warrick
import numpy as np

def f(x):
	val=np.sin(x)
	return val
	
#setting endpoints and number of values	
N=10000
a=0.
b=5.

def riemann_dan(f,a,b,N):
#setting bin width-*
	delta_x=(b-a)/N

#create empty list
	xvals=[]
	yvals=[]
	s=0

#loop over all y values
	for i in range (0,N,1):
#set x val at left endge of bin
		x=a+i*delta_x
#set function value of bin
		y=f(x)
#append x and y to list
		xvals.append(x)
		yvals.append(y)
#increment sum
		s+=y
	s*=delta_x
	return s
	#print(s)
#things converge slowly with Riemann Sum