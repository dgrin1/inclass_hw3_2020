import matplotlib.pyplot as plt
import numpy as np

#go into interactive mode
plt.ion()

#Use Latex fonts
plt.rc('text',usetex=True)
plt.rc('font', family='serif')

#dense x grid for theory curve
x=np.linspace(0,2*3.14159,1000)

#y values for sin good theory
y=np.sin(x)

#y values list for bad sin theory
ybad=np.cos(x)

##two panel subplots


#coarsely gridded "data"
xdata=np.linspace(0,2*3.14159,100)

#make data points obey sin curve
ydata=(np.sin(xdata))

#Add label
a=plt.plot(x,y,label='theory')
plt.setp(a,linewidth=2)

#plot "data"
plt.plot(xdata,ydata,'+',color='r',label='data',markersize=4)

#Plot title
plt.title('Climate change is scary')

#axis labels
plt.xlabel('Time')
plt.ylabel('Height of ocean in meters')

plt.legend(loc=1)


plt.show()
plt.savefig('test.pdf',format='pdf')

