# methods used in tuples 
name = ("sanan" , 7237,"qismat" , "mango" , 124, 432, 23.8 , True,2,2,2)
print(name.count(2)) # it will count how many times 2 appears in tuple 
print(name.index(124)) # it will give youthe index of this value we have to put the value here not the index like list 
print(len(name)) # it will print length of the tuple

# number tuple
t1 = (23 , 5, 87, 67, 9, 90)
print(max(t1))  # 90 largest value
print(min(t1))  # 5 smallest value
print(sum(t1))  #it will print sum of the tuple #281

# Strings tuple
t2 = ("apple", "banana", "mango")
print(min(t2))  # "apple" (alphabetically first)
print(max(t2))  # "mango" (alphabetically last)

# max tuple will give an error for finding min and max value 
# operators in tuple 

t = (1, 2, 3)
print(2 in t)   # True
print(5 in t)   # False
