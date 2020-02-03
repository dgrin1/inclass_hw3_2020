

#loop to make sure it is an integer and not a string or float or something
while True:
  try:
    N = int(input("Please choose the value to sum up to: "))
    break
  except ValueError:
    print("No, it has to be an integer")

#set vars in preparation for sum
n = 1
sumthing = 0


#while loop to sum up over series
for n in range(1,N+1):
  #adds each new term to the sum starting from n=1
  sumthing += 1/n
  #moves on to the next n
  n += 1




print("Your sum over N is ",sumthing)
