import matplotlib.pyplot as plt
import numpy as np

def riemann_integrate_method(f,a,b,N):
    deltX = (b-a)/N
    s=0
    for i in range(1,N):
        s += f(a+i*deltX)
    return s*deltX
    
print("riemann gives", riemann_integrate_method(lambda x: x**4-2*x+1,0,2,1000))

def trapezoid_integrate_method(f,a,b,N):
    deltX = (b-a)/N
    s=0
    for i in range(1,N):
        s += f(a + i*deltX)
    return (b-a)/(2*N)*(f(a)+f(b)+2*s)


print("trapezoids give", trapezoid_integrate_method(lambda x: x**4-2*x+1,0,2,1000))

def simpson_integrate_method(f,a,b,N):
    h = (b-a)/N
    sEven=0
    sOdd = 0
    for k in range(2,N,2):
        sEven += f(a + k*h)
    for k in range(1,N,2):
        sOdd += f(a+k*h)
    return h/3*(f(a)+ 4*sOdd + 2*sEven + f(b))


print("simpson gives", trapezoid_integrate_method(lambda x: x**4-2*x+1,0,2,1000))

f = lambda x: x**4-2*x+1

nvals = np.arange(4,400,2)
RiemVals = [riemann_integrate_method(f,0,2,n) for n in nvals]
TrapVals = [trapezoid_integrate_method(f,0,2,n) for n in nvals]
SimpVals = [simpson_integrate_method(f,0,2,n) for n in nvals]

totalVals = [RiemVals, TrapVals, SimpVals]

labels = ["Left Riemann","Trapezoid","Simpsons"]

for a in len(total:
   plt.plot(nvals,a,)

plt.show()