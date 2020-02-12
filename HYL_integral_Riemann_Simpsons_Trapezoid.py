# 02/10/2019   
# inclass work for integration

from numpy import *

# Left Riemann Sum
def RiemannSum(f,a,b,N):
    sum=0.0
    delta=float(abs(b-a)/N)
    for i in range(N):
        sum+=f(a+i*delta)
    sum *=delta
    return sum
    

# test
print(RiemannSum(sin,1,2,1000000))
print("Difference from the theoretical value is: ",abs(RiemannSum(sin,1,2,1000000)-0.9564491424152821))
print("\n")


# Simpsons Sum (using extended Simpson's rule in chapter 5 p146 of Newman)
def SimpsonsSum(f,a,b,N):
    sum1=0.0
    sum2=0.0
    sum=0.0
    delta=float(abs(b-a)/N)
    # Odd terms 
    for i in range(1,N,2):
        sum1+=f(a+i*delta)
    sum1*=4
    # Even terms
    for j in range(2,N,2):
        sum2+=f(a+j*delta)
    sum2*=2
    # Finalize the sum
    sum = (1/3)*delta*(sum1+sum2+f(a)+f(b))
    return sum

# test
print(SimpsonsSum(sin,1,2,1000000))
print("Difference from the theoretical value is: ",abs(SimpsonsSum(sin,1,2,1000000)-0.9564491424152821))
print("\n")


# Trapezoid Sum (using equation in chapter 5 p142 of Newman)
def TrapezoidSum(f,a,b,N):
    delta=float(abs(b-a)/N)
    sum=0.0
    for i in range(1,N):
        sum+=f(a+i*delta)
    sum=sum+(1/2)*(f(a)+f(b))
    sum*=delta
    return sum

# test
print(TrapezoidSum(sin,1,2,1000000))
print("Difference from the theoretical value is: ",abs(TrapezoidSum(sin,1,2,1000000)-0.9564491424152821))
print("\n")