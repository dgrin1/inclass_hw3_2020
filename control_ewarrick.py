whole=int(input("Choose an integer less than 7"))
#read in a number

control= whole > 7
if control==True:
	print(whole, "is larger than 7. You chose badly. I will fix that for you.")
	whole=5
	print(whole,"is smaller than 7. Better choice. Ha ha!")
#elif whole>5:
#	print("You're ok but cutting it awfully close.")
else:
	print("Great job.")