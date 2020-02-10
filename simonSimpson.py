import numpy as np

step = input("say a step size: ")
summ = 0
xx = np.linspace(0,2, step)
funn = (xx**4)-(2*xx)+1


for x in range(1,step-1, 2):
    summ += (2/(3*step))*(funn[x]+)

print(summ)