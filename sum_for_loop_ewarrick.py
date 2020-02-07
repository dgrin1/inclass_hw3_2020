#a code that goes through the sum same as last time but with a for loop
#collaborators: Nina

#input a number of iterations
num=int(input("please enter a number: "))

#initial statement

#start at n=1 for the sum
n=1.0
#empty harmonic
harmonic=0.0

#perform sum using while loop
for n in range(1,num):
 	harmonic=1/n + harmonic
 	n=n+1
print(harmonic)