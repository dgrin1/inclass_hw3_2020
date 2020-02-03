sum = 0.0

max = float(input("say a number?: "))

for i in range(1,int(max+1)):
    sum += 1.0/i
    
print(sum)