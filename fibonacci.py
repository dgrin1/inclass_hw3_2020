n=int(input(""))
def fibonacci(n):
	if n == 0:
		return 1
	if n>0:
		return fibonacci(n-2) + fibonacci(n-1)
print(fibonacci(n))