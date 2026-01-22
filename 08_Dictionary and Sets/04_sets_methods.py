s = {12, 43.8, "sanny", "sahil", True, 3,3,3}
print(s) # no repetition + random print 

print(len(s))

s.add("shalmani") # add item to the set
print(s)

s.remove("sanny") # remove an item (give error if not found the element)
print(s)

s.discard("aqib") # discard also remove element (if element not found , no error)
print(s) 

s.pop() # remove a random item
print(s)

s.clear() # clear all the set
print(s)

