# 2. Write a program to greet all the person names stored in a list ‘l’ and which starts
# with S.
# l = ["Harry", "Soham", "Sachin", "Rahul"]

l = ["Harry", "Soham", "Sahil", "Rahul", "Sanan", "sanny", "sannu7"]
for name in l:

    if(name.startswith("S")):
        print("Hello",{name})
        

    if name.lower().startswith("s"):
        print(f"Hello {name}")