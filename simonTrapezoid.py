import numpy as np

step = input("say a step size: ")
summ = 0
xx = np.linspace(0,2, step)
funn = (xx**4)-(2*xx)+1


for x in range(step-1):
    summ += (funn[x]+funn[x+1])/step

print(summ)