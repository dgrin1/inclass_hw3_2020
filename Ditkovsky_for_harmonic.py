import numpy as np

n = int(input('How many harmonics?'))

#initialize sum
sum = 0

#iterate up to n
for i in range(n):
	sum += 1/(float(i+1))
	
print('the harmonic sum is %s' %(sum))