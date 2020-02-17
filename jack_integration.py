import numpy as np
import matplotlib.pyplot as plt
#define the function
def f(x):
	val = x**4 - 2*x + 1
	return val
#set the initial value for the integral
N=10000
A=0.
B=2.

#define the sum
def reimman_jack(f,A,B,N):
#set the bin size
	delta_x = (B-A)/N
	#set s to zero
	s=0
	
	#begin the summation loop that will do it N many times
	for i in range(0,N,1):
		#setting x to the value on the left side of the rectangle
		x=A+i*delta_x
		#evaluating the function at said x value
		y=f(x)
		#adding that value to y
		s+=y
	#multiplying the eventual sum by delta_x to since that is the area
	s*=delta_x
	return s
	#printing the seult
print(reimman_jack(f,A,B,N))
#defining the trapezoidal integration
def trapez_jack(f,A,B,N):
	#setting the step size
	delta_x = (B-A)/N
	#setting the sum value to zero at the start
	s=0
	for i in range(0,N,1):
		#defining at what value x will be evaluated
		x=A+i*delta_x
		#now we evaluate f(x) at x and the step after x and divide by 2 to get average value of the 2
		y=(f(x)+f(x+delta_x))/2
		#add it to y
		s+=y
	#multiply the resulting sum by delta_x to get the area under the curve
	s*=delta_x
	return s
#Printing the value
print(trapez_jack(f,A,B,N))
#same as before
def simpson_jack(f,A,B,N):
	#same step size as last time
	delta_x = (B-A)/N
	so=0
	#now I am setting 2 different loops, one for the even values and one for the odd values
	#this one is for odd
	for i in range(1,N,2):
		x=A+i*delta_x
		y=f(x)
		so+=y
	
		
	se=0	
	#this loop s for the even values
	for i in range(2,N,2):
		x=A+i*delta_x
		y=f(x)
		se+=y
	#now I have two separate sums that I am then all adding up to calculate the simpson method of the integral
	return delta_x/3*(f(A)+f(B)+4*so+2*se)
#printing it
print(simpson_jack(f,A,B,N))
		