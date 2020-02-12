import numpy as np
import matplotlib.pyplot as plt

def poly(x):
	return (x**4 - 2*x +1)

def riemann(func, n, xmin, xmax):
	array = np.linspace(xmin, xmax, n)
	
	arrayfunc  = func(array)
	integral = 0
	bins = (xmax - xmin) /n

	for i in range(len(arrayfunc) -1 ):
		integral +=  bins * arrayfunc[i]

	return integral

def trapazoid(func, n, xmin, xmax):
	array = np.linspace(xmin, xmax, n)
	arrayfunc  = func(array)
	integral = 0

	bins = (xmax - xmin) /n

	for i in range(len(arrayfunc) -1 ):
		integral += bins * (arrayfunc[i] + arrayfunc[i+1])/2

	return integral

def simpson(func, n, xmin, xmax):
	array = np.linspace(xmin, xmax, n)
	arrayfunc  = func(array)
	integral = arrayfunc[0] + arrayfunc[-1]

	bins = (xmax - xmin) /n

	for i in range(len(arrayfunc) -2 ):
		if (i+1) %2 == 0: 		#even
			integral += 4 * arrayfunc[i+1]
		else:
			integral += 2 * arrayfunc[i+1]
	return ((bins/3) * integral)

def analytic(xmin, xmax):
	start = (3*xmin**3-2)
	end = (3*xmax**3-2)
	return (end-start)

def error(nfunc, afunc, func, Nmin, Nmax, xmin, xmax):
	Narray = np.arange(Nmin, Nmax, 1)
	error_dist = []

	for N in Narray:
		analy = afunc(xmin, xmax)
		numeric = nfunc(func, N, xmin, xmax)
		
		term = (analy - numeric) /analy
		error_dist.append(term)

	return error_dist

Ndomain = np.arange(100, 1000, 1)
trapacurve = error(trapazoid, analytic, poly, 100, 1000, 0, 1000)
simpcurve = error(simpson, analytic, poly, 100, 1000, 0, 1000)
riecurve = error(riemann, analytic, poly, 100, 1000, 0, 1000)

plt.plot(Ndomain, trapacurve, label="trapazoid curve")
plt.scatter(Ndomain, simpcurve, label="simpson curve")
plt.plot(Ndomain, riecurve, label="reimann curve")

plt.legend()
plt.show()
