import numpy as np

step = input("say a step size: ")
summ = 0
xx = np.linspace(0,2, step, endpoint = False)
funn = (xx**4)-(2*xx)+1


for x in funn:
    summ += (x*2/step)

print(summ)