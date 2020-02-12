sum = 0

N = int(input("Give an integer"))

for i in range(N):
	sum += 1/(i+1)
print(sum)