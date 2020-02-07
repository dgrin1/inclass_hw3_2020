# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 13:43:52 2020

@author: shaun
"""
x=int(input("enter the number of terms in your harmonic series"))
sumx=0
for i in range(1,x):
    sumx+=1/i
print(sumx)