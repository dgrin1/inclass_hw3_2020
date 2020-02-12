import numpy as np

step = input("say how many steps: ")
sum1 = 0
sum2 = 0
h = float(2)/(step-1)
xx = np.linspace(0,2, step)
funn = ((xx**4)-(2*xx)+1)


for x in range(1,step, 2):
    sum1 += funn[x]
    
for x in range(2,step, 2):
    sum2 += funn[x]

print((h/3)*(funn[0]+funn[2]+4*sum1+2*sum2))