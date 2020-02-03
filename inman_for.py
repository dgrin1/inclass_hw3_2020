#requests the number of iterations from user
iterations = int(input("How many harmonics? "))

#initializes variables
N = 1.0
sum = 0.0

#computes the sum from 1 -> user input
for i in range(1,iterations):
	sum = sum + (1 / i)
	#iterates the input
	#i = i + 1

print("The result is: ", sum)
