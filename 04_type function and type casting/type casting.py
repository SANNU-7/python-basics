# typecasting mean changing one data type to another data type like string to float , float to integer and so on...


a = 19
b = float(a)
t = type(b)
print(t)  # it will print float because we change integer to float 


# w = "Sanan Shah"
# y = float(w)
# s = type(y)
# print(s)  this will not print Because typecasting works only when the string looks like a number.

# for example 

w = "786"
y = int(w)
s = type(y)
print(s) # it wil print string as a float


# str to bool
w = "786"
y = bool(w)
s = type(y)
print(s) 

# bool to float
w = False
y = float(w)
s = type(y)
print(s)


w = "sanan shah"
y = bool(w)
s = type(y)
print(s)