import matplotlib.pyplot as plt
import numpy as np
#plt.ion only works in interactive mode
#plt.ion()
#plt.rc('text',usetex=True)
plt.rc('font', family='sans-serif')
#plt.rc('font', sans-serif='Tahoma')

x=np.linspace(0,2*np.pi,100)
y=np.exp(np.sin(x))
x2=np.linspace(0,2*np.pi,15)
y2=np.exp(5*np.sin(x2))
x3=no,linspace(0,2+np.pi,15)
y3=np.exp(5*np.sin(x+.4))
plt.yscale('log')
plt.xscale('log')
plt.plot(x,y, 'red')
plt.plot(x2,y2, 'k*', label='thin mint')
plt.plot(x3,y3,'r*', label='peanut butter patty')
plt.legend(loc=1)
plt.grid()
plt.xlim([2,7])
plt.xlabel(r'$~\Gamma$')
plt.ylabel('girl scout cookies eaten')
plt.show