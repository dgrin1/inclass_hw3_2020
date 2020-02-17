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

def trapez_jack(f,A,B,N):
	delta_x = (B-A)/N
	
	s=0
	for i in range(0,N,1):
		x=A+i*delta_x
		y=(f(x)+f(x+delta_x))/2
		s+=y
	s*=delta_x
	return s
print(trapez_jack(f,A,B,N))

def simpson_jack(f,A,B,N):
	delta_x = (B-A)/N
	so=0
	for i in range(1,N,2):
		x=A+i*delta_x
		y=f(x)
		so+=y
	
		
	se=0	
	for i in range(2,N,2):
		x=A+i*delta_x
		y=f(x)
		se+=y
	
	return delta_x/3*(f(A)+f(B)+4*so+2*se)
print(simpson_jack(f,A,B,N))
		