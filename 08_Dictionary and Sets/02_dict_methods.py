# consider the following dictionary

name = {
    "name" : "Sanan shah",
    "age" : 19,
    "country" : "pakistan",
    "marks" : 67,
    "lst" : [34, 43, 67, 78.5]
    
    }
print(len(name)) 

print(name.get("name")) # Returns the value of the specified keys if key was not present in the dictionary it will return none 

print(name["name"]) # return also the key if key is not present in dictionary it will return an error

print(name.items()) # Returns key–value pairs

name.update({"village": "nagoha", "percentage": 91}) # update the dictionary
print(name) 

print(name.keys()) # returns all keys

print(name.values()) # returns all values

name.pop("percentage") # remove the key 
print(name)

name.popitem() # remove last item in the  dictionary
print(name)