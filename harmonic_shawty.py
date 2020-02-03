N=int(input("choose an INTEGER greater than 1: "))
n=1
s=0
a_n=1/n
while n<=N:
	#print(1/n)
	n=n+1
	next=1/n
	s+=next
print(s)
