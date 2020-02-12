# 02/10/2019   
# inclass work for integration

import numpy as np 
import matplotlib.pyplot as plt
import scipy.integrate as integrate

# Left Riemann Sum
def RiemannSum(f,a,b,N):
    sum=0.0
    delta=float(abs(b-a)/N)
    for i in range(N):
        sum+=f(a+i*delta)
    sum *=delta
    return sum
    
'''
# test
print(RiemannSum(lambda x: x**4-2*x+1,2,0,1000000))
print("Difference from the theoretical value is: ",abs(RiemannSum(lambda x: x**4-2*x+1,2,0,1000000)-4.4))
print("\n")
'''

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
'''
# test
print(SimpsonsSum(lambda x: x**4-2*x+1,2,0,1000000))
print("Difference from the theoretical value is: ",abs(SimpsonsSum(lambda x: x**4-2*x+1,2,0,1000000)-4.4))
print("\n")
'''

# Trapezoid Sum (using equation in chapter 5 p142 of Newman)
def TrapezoidSum(f,a,b,N):
    delta=float(abs(b-a)/N)
    sum=0.0
    for i in range(1,N):
        sum+=f(a+i*delta)
    sum=sum+(1/2)*(f(a)+f(b))
    sum*=delta
    return sum

# The function for testing (one could also use lambda x : x**4-2*x+1)
def function(x):
    return x**4-2*x+1

'''
# test
print(TrapezoidSum(function,0,2,100))
print("Difference from the theoretical value is: ",abs(TrapezoidSum(function,0,2,100)-4.4))
print("\n")
'''

# Create plots for the numerial integration result, the theoretical result & their difference as errors vs. N
def plot(f,a,b,N):

    # Clear figure for fresh start
    plt.clf()
    # Go into interactive mode
    plt.ion()
    # Use Latex fonts
    plt.rc('text',usetex=True)
    plt.rc('font', family='serif')

    # Dense x grid for theory curve
    x=np.linspace(1,N,N)
    # y values as the integration result for theory. Note that integrate.quad(f,a,b) gives you a tuple of the integration result & its error, so we only want the first one
    y=np.linspace(integrate.quad(f,a,b)[0],integrate.quad(f,a,b)[0],N)

    # x values for riemann & trapezoid curves
    xdata=np.linspace(1,N,N-1)
    # x values for simpsons curve (need to be even)
    xdata_simp = np.linspace(2,N,int(N/2))

    # Initialize arrays for storing data points
    y_riemann=np.array([])
    y_trapezoid=np.array([])
    y_simpsons=np.array([])

    # Data points for error
    error_riemann = np.array([])
    error_trapezoid = np.array([])
    error_simpsons = np.array([])

    for i in range (1,N):
        y_riemann=np.append(y_riemann,RiemannSum(f,a,b,i))
        y_trapezoid=np.append(y_trapezoid,TrapezoidSum(f,a,b,i))
    
    for k in range (2,N+2,2):
        y_simpsons=np.append(y_simpsons,SimpsonsSum(f,a,b,k))

    for j in range(1,N):
        error_riemann = np.append(error_riemann, y_riemann[j-1]-y[0])
        error_trapezoid = np.append(error_trapezoid, y_trapezoid[j-1]-y[0])
    
    for l in range(0,int(N/2)):
        error_simpsons = np.append(error_simpsons, y_simpsons[l]-y[0])

    ## Two panel subplots
    fig, ax = plt.subplots(2,sharex=True)

    # Plot "theory" on subplot 1
    ax[0].plot(x,y,'-',color='#ffaf0f80',label='Theory',linewidth=2)
    # Plot "riemann" on subplot 1 as well
    ax[0].plot(xdata,y_trapezoid,'+',color=(0.5,0.1,0.25),label='Trapezoid',markersize=2)
    # Plot "trapezoid" on subplot 1 as well
    ax[0].plot(xdata,y_riemann,'*',color=(0.25,0.1,0.5),label='Riemann',markersize=2)
    # Plot "simpsons" on subplot 1 as well
    ax[0].plot(xdata_simp,y_simpsons,'.',color=(0.1,0.5,0.25),label='Simpsons',markersize=2)
    
    # Subplot axis labels
    ax[0].set_ylabel('Integration Results \n' r'$(y_{true}=4.4)$')

    # Plot "theory" on subplot 1
    ax[1].plot(x,np.linspace(0,0,N),'--',color='k',linewidth=2)
    # Plot "riemann" on subplot 1 as well
    ax[1].plot(xdata,error_trapezoid,'H',color=(0.7,0.7,0.25),label='Trapezoid Errors',markersize=2)
    # Plot "trapezoid" on subplot 1 as well
    ax[1].plot(xdata,error_riemann,'h',color=(0.25,0.7,0.7),label='Riemann Errors',markersize=2)
    # Plot "simpsons" on subplot 1 as well
    ax[1].plot(xdata_simp,error_simpsons,'o',color=(0.7,0.25,0.7),label='Simpsons Errors',markersize=2)
    
    # Subplot axis labels
    ax[1].set_ylabel('Errors for Different\n Numerical Integrations Methods')

    # Enable grid
    ax[0].grid(linestyle='-', linewidth=0.1)
    ax[1].grid(linestyle='-', linewidth=0.1)

    # Common x label
    plt.xlabel('Numbers of Iteration N')

    # Title for both subplots
    fig.suptitle('Numerical \& theoretical integration results vs. N')
    
    # Include legends separately for suplots
    ax[0].legend(loc=1,prop={'size': 6})
    ax[1].legend(loc=1,prop={'size': 6})

    # Show & save the figure
    fig.show()
    fig.savefig('HYL_integral.pdf',format='pdf')




# test (Note that N is better be an even integer)
plot(function,0,2,100)