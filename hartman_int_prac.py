
from math import pi
from numpy import cos,sin,linspace,exp
from pylab import plot,show,xlabel,ylabel,title,savefig


def f(x):
	val = x**(4) -2*x +1
	return val

N=100000
a=0.
b=2.


# Left Riemann Sum
def RiemannSum(f,a,b,N):
    s=0.0
    delta=float(abs(b-a)/N)
    for i in range(N):
        sum+=f(a+i*delta)
    s *=delta
    return s




#plotting and displaying the plot
plot(delta, s)
show()

#def simpson_hartman(f,a,b,N):

def SimpsonsSum(f,a,b,N):
    sum1=0.0
    sum2=0.0
    sum=0.0


    delta=float(abs(b-a)/N)


    # to get the odd terms
    for i in range(1,N,2):
        sum1+=f(a+i*delta)
    sum1*=4



    # Even terms
    for j in range(2,N,2):
        sum2+=f(a+j*delta)
    sum2*=2



    # combining the odd and even sums
    sum = (1/3)*delta*(sum1+sum2+f(a)+f(b))
    return sum


# #def trapazoid_hartman(f,a,b,N):
# 	delta_x2 = (b-a)/N
#
# 	xvals2=[]
# 	yvals2=[]
#
# 	for i in range(0,N,1):
# 		x=
