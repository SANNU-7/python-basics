data = [123, 6.765, True, "sanan","pakistan", "apple"]
print(data)
#  methods which we use to change this original data without creating a new one 

data.append("sahil") # append method add another value to the original list 
print(data)

lst = [21,23,87,100,1,2,2]

lst.sort() # sort method will sort the number in ascending order
lst.reverse() #it will reverse the list
lst.remove(2) #it will remove a single data from list 
lst.insert(3 ,"sanan") #it will insert a value at a specific index you want

print(lst)

lst = [10, 20, 30, 20]
x = lst.pop(1) # will delete element at index 2 and return its value. if no index is given to it it will delete the las element of the list 
print(x)
print(lst)
 
#  to find index in a list 
numbers = [5, 10, 15, 20, 2]
print(numbers.count(2))
print(numbers.index(15)) # directly prints 2

