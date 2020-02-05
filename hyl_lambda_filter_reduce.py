# The use of lambda & map function to quickly manipulate data set
Celcius= [25.5,36,40,18,10]
Fahren = list(map(lambda x:x*(float(9/5))+32, Celcius))
print(Fahren)

list1=[1,2,3]
list2=[4,5,6]
sum_of_list = list(map(lambda x,y:x+y, list1, list2))
print(sum_of_list)

# The use of filter to filter out things based on the boolean result returned by applying a function to a sequence
a = [1,1,2,3,5,8,10,21]
odd = filter(lambda x:x%2, a)
print(list(odd))


# The use of reduce to apply a function on a list of arguments
from functools import reduce
b = [1,2,3]
# Add all elements of the list
sum = reduce(lambda x,y:x+y, b)
print(sum)