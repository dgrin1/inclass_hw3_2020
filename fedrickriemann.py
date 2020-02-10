# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 12:57:50 2020

@author: shaun
"""
import numpy as np
def rpart(y1,y2,delta):
    sumx=((y1+y2)/2)*delta
    return sumx
def function(x):
    function=(x**4)-(2*x)+1 
    return function
def rwhole(N,a,b):
    listx=np.linspace(a,b,N)
    sumx=0
    for x in range(0,N):
        if(x<N-1):
            y1=function(listx[x])
            y2=function(listx[x+1])
            delta=listx[x]-listx[x+1]
            delta=(delta**2)**(0.5)
            sumx+= rpart(y1,y2,delta)
        else :
            return sumx
        

print(rwhole(1000,0,2))   