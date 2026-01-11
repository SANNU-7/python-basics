# String is a data type in python.
# String is a sequence of characters enclosed in quotes.
# We can primarily write a string in these three ways.

a ='harry' # Single quoted string
b = "harry" # Double quoted string
c = '''harry''' # Triple quoted string



# slicing of character
name = "Harry"
nameshort = name[0:3] # start from index 0 all the way till 3 (excluding 3)
print(nameshort)
character1 = name[1]
print(character1)



# String immutability means:
# 👉 You cannot change a string after it is created.
# Example:
# name = "Harry"
# name[0] = "S"   # ❌ Error
