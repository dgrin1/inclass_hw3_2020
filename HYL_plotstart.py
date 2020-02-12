import matplotlib.pyplot as plt
import numpy as np
#import matplotlib.font_manager as font_manager

#font_manager._rebuild()
'''
String variable with Tex enable should be careful when using symbol like "_", which needs to be "\_" instead
'''

#go into interactive mode
plt.ion()
#Use Latex fonts
plt.rc('text',usetex=True)
#plt.rc('font', family='serif')

''' The tex font not found solution could be: https://matplotlib.org/1.3.1/users/usetex.html'''

#plt.rc('font',**{'family':'sans-serif','sans-serif':['Helvetica']})
## Using Palatino font (terminal might print warning):
plt.rc('font',**{'family':'serif','serif':['Palatino']})

#dense x grid for theory curve
x=np.linspace(0,2*3.14159,1000)

#y values for sin good theory
y=np.sin(x)

#y values list for bad sin theory
ybad=np.cos(x)

#coarsely gridded "data"
xdata=np.linspace(0,2*3.14159,50)

#make data points obey sin curve
ydata=(np.sin(xdata))



##two panel subplots
fig, ax = plt.subplots(2)

#Plot "theory" on subplot 1
ax[0].plot(x,y,'-.',color='#0f0f0f80',label='theory',linewidth=2)

#plot "data" on subplot 1 as well
ax[0].plot(xdata,ydata,'+',color=(0.5,0.1,0.25),label='data',markersize=5)

# Setting percetage error bar for "data"
xerror = 0.1  
yerror = 0.2 
ax[0].errorbar(xdata, ydata, xerr=xdata*xerror, yerr=ydata*yerror, color="black", barsabove='False',capsize=1, capthick=0.5,linewidth=0.5)

#subplot axis labels
ax[0].set_xlabel('Time'r'$~\Gamma$')
ax[0].set_ylabel('Height of ocean in meters')




# Subplot 2 with transformations applied to "theory" & "data"
y_new = abs(np.exp(-x)*np.sin(x))
ydata_new = abs(ydata)

# Plot y_new & ydata_new on subplot 2
ax[1].plot(x,y_new,'--',color='#0fffff80',label='theory\_transformed',linewidth=2)
ax[1].plot(xdata,ydata_new,'.',color=(0.1,0.1,0.6),label='data\_transformed',markersize=5)

# Setting the logarithmic y-axis for the subplot 2 
ax[1].set_yscale('log')

#subplot axis labels
ax[1].set_xlabel('Time'r'$~\Gamma$')
ax[1].set_ylabel('Logarithmic Height of ocean in meters')



# Gloabal setting for the fig/plot:

# Title for both subplots
fig.suptitle('Climate change is scary')

# Allow some spacings between subplots
fig.tight_layout()

# Add margin on the top for the fig
fig.subplots_adjust(top=0.8)

fig.legend(loc=1)

fig.show()
fig.savefig('HYL_test.pdf',format='pdf')
