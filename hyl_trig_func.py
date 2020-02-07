import numpy as np
import math

def hyl_sin(x):
    x = x%(2.e0*np.pi)
    i = 0
    s,sold = 0.e0,0.e0
    for i in range (100000):
        sold = s
        s+= float((((-1)**i) * (x**((2*i) + 1))))/float(math.factorial(((2*i) + 1)))
        if sold==s: break
    return s
    

def hyl_cos(x):
    x = x%(2.e0*np.pi)
    i = 0
    s,sold = 0.e0,0.e0
    for i in range (100000):
        sold = s
        s+= float((((-1)**i) * (x**(2*i))))/float(math.factorial((2*i)))
        if sold==s: break
    return s


def hyl_tan(x):
    return hyl_sin(x)/hyl_cos(x)


def hyl_sec(x):
    return 1.e0/hyl_cos(x)


def hyl_cosec(x):
    return 1.e0/hyl_sin(x)


def hyl_cot(x):
    return 1.e0/hyl_tan(x)
