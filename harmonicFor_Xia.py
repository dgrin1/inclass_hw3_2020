# Using while 
# harmonicNum = 0
# i=1
# while i<=n :
# 	harmonicNum = harmonicNum + 1/i
# 	i +=1

# print ("the %dth harmonic number is %1.3f" % (n,harmonicNum))

# Use for loop:
def harmonic(n):
	sum =0
	for i in range(n):
		sum +=1/(i+1)
	return sum

n = int(input("n:"))
print("%d th harmonic number is %1.2E"%(n,harmonic(n)))