
s = "sanan"
print(len(s)) # this show length of the string
print(s.endswith("an")) # it show that the string ending with the mentioned char is true or false
print(s.startswith("sa")) # it show that the string start with the mentioned char is true or false
print(s.capitalize()) # capitalizes only the first character of the whole string


name = "sanan shah"
print(name.upper() )  # SANAN
print(name.lower() )  # sanan
print(name.title()  ) # capitalizes first character of every word
print(name.replace("n","p"))# sapap
print(name.find("a") )      # 1
print(name.count("a")   )   # 2


name = " sanny "
print(name)
print(name.strip()   )      # remove extra spaces of the side not middle

text = "Sanan Shah Ai"
print(text.split()) # It breaks a string into a list
